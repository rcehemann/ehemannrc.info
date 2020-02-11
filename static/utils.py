import re

with open("static/docs/resume.tex", "r") as f:
	lines = "".join(f.readlines())

regex = {
	'items' : re.compile(r".*?\\item (.*?)\n.*?"),
	'entries' : re.compile(r".*?\\entry.*?\((.*?)\).*?\((.*?)\).*?\((.*?)\).*?\((.*?)\).*?",
							re.MULTILINE|re.DOTALL)
}

def clean(element):
	element = re.sub(r"{?\\emph{(.*?)}}?", r"<em>\1</em>", element)
	element = re.sub(r"{?\\bf{(.*?)}}?", r"<strong>\1</strong>", element)
	element = re.sub(r"\\&", r"&", element)
	return element.strip()

def parse_cv_section(title, pattern='items'):
	section = list(filter(lambda s: title in s, lines.split('\\cvsect')))[0]
	elements = regex[pattern].findall(section)

	if pattern == 'items':
		return list(map(clean, elements))
	elif pattern == 'entries':
		print(r"{}".format(section))
		return elements

if __name__ == '__main__':
	print(parse_cv_section("Experience", pattern='entries'))
	print(parse_cv_section("Education", pattern='entries'))
	print(parse_cv_section("Publications", pattern='items'))
	print(parse_cv_section("Presentations", pattern='items'))
	print(parse_cv_section("Awards \\& Honors", pattern='items'))