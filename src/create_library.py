from lxml import etree
from lxml.builder import E
import json
import rdflib
from rdflib import Graph, URIRef, Namespace, util
from rdflib.util import SUFFIX_FORMAT_MAP
from rdflib.namespace import NamespaceManager, RDFS, RDF, XSD, SKOS, OWL
import re
import base64
import zlib
from urllib.parse import quote, unquote, quote_from_bytes
import argparse

SUFFIX_FORMAT_MAP["rdfs"] = "xml"
SUFFIX_FORMAT_MAP["rdf"] = "xml"
SUFFIX_FORMAT_MAP["json"] = "json-ld"

def parseOnto(g):
	ontoParse = []
	entities = {}
	for c in g.subjects(RDF.type, RDFS.Class):
		e = c.n3().rpartition('/')[-1].rpartition('#')[-1].replace('>','')
		meta = {'type': 'class', 'data': {'URI': c.n3().replace('<','').replace('>','')}}
		spcList = []
		l = 0	# l is the level/depth of the hierarchy
		while l <= 9: 
			if l == 0:
				sc = c
			for spc in g.objects(sc, RDFS.subClassOf):
				if not isinstance(spc, rdflib.BNode):
					spcList.append(spc.n3().rpartition('/')[-1].rpartition('#')[-1].replace('>',''))
					sc = spc
			l += 1
		meta['spc'] = spcList
		labels = {}
		for o in g.objects(c,RDFS.label):
			labels[o.language] = o
		meta['data']['labels'] = labels
		entities[e] = meta

	for p in g.subjects(RDF.type, RDF.Property):
		e = p.n3().rpartition('/')[-1].rpartition('#')[-1].replace('>','')
		meta = {'type': 'prop', 'data': {'URI': p.n3().replace('<','').replace('>','')}}
		labels = {}
		for o in g.objects(p,RDFS.label):
			labels[o.language] = o
		meta['data']['labels'] = labels
		entities[e] = meta
		for note in g.objects(p,RDFS.comment):
			quants = re.match('.*\(([\d\w],[\d\w])\:([\d\w],[\d\w])\)',note)
			if quants:
				meta['data']['quants'] = [quants.group(1),quants.group(2)]
	return entities

def classDict(colors,baseOnto,extOnto=None):
	d = {"Instance": {
		'type': 'class',
		'color': '#ffffff',
		'data': {
	        'URI': 'https://example.org/instance_uri', 'labels': {}
            }
		}
	}


	# base CIDOC-CRM
	cidoc = parseOnto(baseOnto)
	for e in cidoc:
		if cidoc[e]['type'] == 'class':
			for spc in cidoc[e]['spc']:
				# spc = spc.split(':')[1]
				if spc in colors:
					cidoc[e]['color'] = colors[spc]
					# d[sc] = colors[spc]
					break 
					# exit loop after the first superclass is found in the colors list.
					# e.g. for 'E21_Person' the first superclass found in the colors list
				# is E39_Actor
	for c in colors:
		if c in cidoc:
			cidoc[c]['color'] = colors[c]

	if extOnto:
		extension = parseOnto(extOnto)
		# extClass = extension[0]
		for ent in extension:
			if extension[ent]['type'] == 'class':
				if ent in colors:
					extension[ent]['color'] = colors[ent]

				elif ent in cidoc:
					extension[ent]['color'] = cidoc[ent]['color']
				else:
					allSpc = extension[ent]['spc']
					for crmSpc in allSpc:
						if crmSpc in colors:
							extension[ent]['color'] = colors[crmSpc]
							break
						elif crmSpc in cidoc:
							extension[ent]['color'] = cidoc[crmSpc]['color']
							break
						elif crmSpc in extension:
							if 'color' in extension[crmSpc]:
								extension[ent]['color'] = extension[crmSpc]['color']
								break
							else: continue
						
						else:
							if crmSpc == allSpc[-1]:
								extension[ent]['color'] = '#ffffff'
		d.update(extension)
	else:
		d.update(cidoc)
	return d


# Encoding / Decoding
def js_encode_uri_component(data):
    return quote_from_bytes(data, safe='~()*!.\'')


def js_decode_uri_component(data):
    return unquote(data)


def js_string_to_byte(data):
    return bytes(data, 'iso-8859-1')


def js_bytes_to_string(data):
    return data.decode('iso-8859-1')


def js_btoa(data):
    return base64.b64encode(data)


def js_atob(data):
    return base64.b64decode(data)

def pako_deflate(data):
    compress  = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 15, 
        memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(js_string_to_byte(js_encode_uri_component(data)))
    compressed_data += compress.flush()
    return compressed_data

def pako_deflate_raw(data):
    compress = zlib.compressobj(
        zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15, memLevel=8,
        strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed_data = compress.compress(js_string_to_byte(js_encode_uri_component(data)))
    compressed_data += compress.flush()
    return compressed_data

def pako_inflate(data):
    decompress = zlib.decompressobj(15)
    decompressed_data = decompress.decompress(data)
    decompressed_data += decompress.flush()
    return decompressed_data

def pako_inflate_raw(data):
    decompress = zlib.decompressobj(-15)
    decompressed_data = decompress.decompress(data)
    decompressed_data += decompress.flush()
    return decompressed_data


def compile_style(styleJSON,baseOnto,extOnto=None):
	f = open(styleJSON,'r',encoding='utf-8')
	style = json.load(f)
	updateStyle = style
	colors = style['colors']

	if extOnto is None:
		g = Graph()
		g.parse(baseOnto)
		allCRM = classDict(colors,g)
	else:
		g = Graph()
		g.parse(extOnto)
		baseG = Graph()
		baseG.parse(baseOnto)
		allCRM = classDict(colors,baseG,g)
		
	if 'entities' not in style:
		updateStyle['entities'] = allCRM
	else:
		updateStyle['entities'].update(allCRM)
	f = open(styleJSON,'w',encoding='utf-8')
	f.write(json.dumps(updateStyle, indent=4, ensure_ascii=False))
	return (style,allCRM)

def main(styleJSON,filename,baseOnto,extOnto,has_metadata,with_quant,lang):
	lib = []
	compileStyle = compile_style(styleJSON,baseOnto,extOnto)
	styleDict = compileStyle[0]
	
	# map for titles addition by language tags
	addition = {'en': ' (with quantifications)', 'fr': ' (avec quantifications)'}

	if has_metadata is False:
		xml1 = f'<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;fontSize={styleDict["font"]["size"]["class"]};fontStyle={styleDict["font"]["style"]}" value="E39_Actor" URI="https://example.org" vertex="1"><mxGeometry as="geometry" height="{styleDict["dim"]["height"]}" width="{styleDict["dim"]["width"]}"/></mxCell></root></mxGraphModel>'
		xml2 = f'''<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="abcd" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize={styleDict["font"]["size"]["prop"]};fontStyle={styleDict["font"]["style"]};strokeWidth={styleDict["dim"]["strokeWidth"]};" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint as="sourcePoint"/><mxPoint y="60" as="targetPoint"/></mxGeometry></mxCell>
				<mxCell id="3" value="" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="2"><mxGeometry x="-0.8952" y="1" relative="1" as="geometry"><mxPoint as="offset" /></mxGeometry></mxCell>
				<mxCell id="4" value="" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="2"><mxGeometry x="0.7905" y="1" relative="1" as="geometry"><mxPoint as="offset" /></mxGeometry></mxCell>
				</root></mxGraphModel>'''
	else:
		xml1 = f'<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><object label="E39_Actor" URI="https://example.org/E39" linkTarget="_blank" link="https://example.org/E39" id="2"><mxCell parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;fontSize={styleDict["font"]["size"]["class"]};fontStyle={styleDict["font"]["style"]}" vertex="1"><mxGeometry as="geometry" height="{styleDict["dim"]["height"]}" width="{styleDict["dim"]["width"]}"/></mxCell></object></root></mxGraphModel>'
		xml2 = f'''<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><object label="abcd" URI="https://example.org/abcd" linkTarget="_blank" link="https://example.org/abcd" id="2"><mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize={styleDict["font"]["size"]["prop"]};fontStyle={styleDict["font"]["style"]};strokeWidth={styleDict["dim"]["strokeWidth"]};" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint as="sourcePoint"/><mxPoint y="60" as="targetPoint"/></mxGeometry></mxCell></object>
				<mxCell id="3" value="" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="2"><mxGeometry x="-0.8952" y="1" relative="1" as="geometry"><mxPoint as="offset" /></mxGeometry></mxCell>
				<mxCell id="4" value="" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="2"><mxGeometry x="0.7905" y="1" relative="1" as="geometry"><mxPoint as="offset" /></mxGeometry></mxCell>
				</root></mxGraphModel>'''

	entities = compileStyle[1]
	for i in entities:
		entitySplit = i.split('_')
		ID = entitySplit[0]
		entity = entities[i]
		URI = entity['data']['URI']

		# declare shape
		shape = {"xml": "", "w":"","h":"","aspect":"fixed","title":""}
		if entity['data']['labels']:
			if lang in entity['data']['labels']:
				title = ID+" "+entity['data']['labels'][lang]
			elif 'en' in entity['data']['labels']:
				title = ID+" "+entity['data']['labels']['en']
		else:
			title = i
		shape['title'] = title.replace('_',' ')
		if styleDict['space'] == 'underscore':
			shapeLabel = title.replace(' ','_')
		elif styleDict['space'] == 'whitespace':
			shapeLabel = title.replace('_',' ')
		
		if entity['type'] == 'class':
			width = styleDict['dim']['width']
			shape["w"] = width
			shape["h"] = styleDict['dim']['height']
			root = etree.fromstring(xml1)
			e = root.find(".//mxCell[@style]")
			style = e.attrib["style"]
			new_style = re.sub('fillColor=#\w{6}', 'fillColor='+entity['color'], style)
			e.set('style', new_style)
			mxgeo = root.find(".//mxGeometry")
			mxgeo.set('width', str(width))

		else:
			shape["w"] = 1
			shape["h"] = 100
			root = etree.fromstring(xml2)
			e = root.find(".//mxCell[@style]")
			if with_quant is True:
				if 'quants' in entity['data']:
					quants = entity['data']['quants']
					e3 = root.find(".//mxCell[@id='3']")
					e3.set('value',quants[0])
					e4 = root.find(".//mxCell[@id='4']")
					e4.set('value',quants[1])
					shape['title'] += addition[lang]

		if e is not None:
			if has_metadata is False:
				e.set('value', shapeLabel)
			else:
				obj = e.getparent()				
				obj.set('label', shapeLabel)
				obj.set('URI', URI)
				obj.set('link', URI)
				labels = entity['data']['labels']
				for l in labels:
					obj.set(l,labels[l])

			xml = etree.tostring(root)
			a = pako_deflate_raw(xml)
			b = base64.b64encode(a)
			shape['xml'] = js_bytes_to_string(b)
			lib.append(shape)

	lib = json.dumps(lib)
	out = open(filename, "w", encoding="utf-8")
	out.write('<mxlibrary>{}</mxlibrary>'.format(lib))


# argparse arguments
def parse_args():
	parser = argparse.ArgumentParser(description='Create shape library XML')
	parser.add_argument("-s","--style", help='Libraries style JSON filename', required=True)
	parser.add_argument("-f","--filename", help='Shape library XML filename', required=True)
	parser.add_argument("-b","--baseOnto", help='Path to base ontology RDF file', required=True)
	parser.add_argument("-e","--extOnto", help='Path to extension ontology RDF file', default=None)
	parser.add_argument("-m","--metadata", help="Include shape's metatada (URI, labels, link)", action='store_true')
	parser.add_argument("-q","--quantification", help="Include property's quantification", action='store_true',)
	parser.add_argument("-l","--lang", help='Specify the main language of the library, default is "en"', default='en')
	
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	main(args.style, args.filename, args.baseOnto, args.extOnto, args.metadata, args.quantification, args.lang)