import json
from lxml import etree
from lxml.builder import E
import argparse
import re

def main(XML,version,color,space,dim,font,):
	f = open(f'libraries_style_{version}.json','r')
	style = json.load(f)
	entities = style['entities']

	tree = etree.parse(XML)
	root = tree.getroot().find('.//root')

	for cell in root.findall('.//mxCell'):
		label = ''
		p = None
		if cell.get('value'):
			label = cell.get('value')
		else:
			if cell.getparent().tag in ['UserObject','object']:
				p = cell.getparent()
				label = p.get('label')
		
		i = label.replace(' ','_')
		if i in entities:
			entType = entities[i]['type']
			if space is True:
				spaceStyle = style['space']
				if spaceStyle == 'whitespace':
					if p is None:
						cell.set('value',label.replace('_',' '))
					else:
						p.set('label',label.replace('_',' '))
				elif spaceStyle == 'underscore':
					if p is None:
						cell.set('value',label.replace(' ','_'))
					else:
						p.set('label',label.replace(' ','_'))
			if color is True and entType == 'class':				
				new_style = re.sub('fillColor=#\w{6}', 'fillColor='+entities[i]['color'], cell.get('style'))
				cell.set('style', new_style)
			if dim is True:
				if entType == 'class':
					w = style['dim']['width']
					h = style['dim']['height']
					geo = cell.find('mxGeometry')
					geo.set('width',w)
					geo.set('height',h)
				else:
					sw = style['dim']['strokeWidth']
					if 'strokeWidth' in cell.get('style'):
						new_style = re.sub('strokeWidth=\d+','strokeWidth='+sw, cell.get('style'))
					else:
						new_style = cell.get('style')+';strokeWidth='+sw
					cell.set('style',new_style)
			if font is True:
				fontSize = style['font']['size'][entType]				
				if 'fontSize' in cell.get('style'):
					new_style = re.sub('fontSize=\d+','fontSize='+fontSize,cell.get('style'))
				else:
					new_style = cell.get('style')+';fontSize='+fontSize
				cell.set('style',new_style)
				
				fontStyle = style['font']['style']
				if 'fontStyle' in cell.get('style'):
					new_style = re.sub('fontStyle=\d+','fontStyle='+fontStyle,cell.get('style'))
				else:
					new_style = cell.get('style')+';fontStyle='+fontStyle
				cell.set('style',new_style)
			if version != 'v1':
				data = entities[i].get('data')
				if p is None:
					_id = cell.attrib.pop('id')
					_label = cell.attrib.pop('value')
					p = E('object', id=_id, label=_label, linkTarget="_blank")
					p.append(cell)
					root.append(p)
				if data.get('URI'):
					p.set('URI', data['URI'])
					p.set('link',data['URI'])
				if data.get('labels'):
					for (l,v) in data['labels'].items():
						p.set(l,v)
			else:
				if p is not None:
					_id = p.attrib.pop('id')
					_label = p.attrib.pop('label')
					cell.set('id',_id)
					cell.set('value',_label)
					root.append(cell)
					root.remove(p)

	tree.write(f"{XML.rpartition('.')[0]}_{version}.xml", encoding="utf-8", xml_declaration=True, pretty_print=True)

# argparse arguments
def parse_args():
	parser = argparse.ArgumentParser(description='Update diagrams by version of libraries')
	parser.add_argument("XML", help='Path to draw.io XML file (uncompressed)')
	parser.add_argument("version", help='Version of libraries', choices=['v1','v2'])
	parser.add_argument("-c","--color", help='Update color', action='store_true')
	parser.add_argument("-s","--space", help='Update label spacing', action='store_true',)
	parser.add_argument("-d","--dimension", help='Update dimensions, width and height for class, widthStroke for property', action='store_true')
	parser.add_argument("-f","--font", help='Update font (size, style)', action='store_true')
	
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	main(args.XML, args.version, args.color, args.space, args.dimension, args.font)
