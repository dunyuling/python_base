

class HtmlOutputer(object):
    def __init__(self):
        self.datas = [] 

    def collect_data(self, data): 
        if data is None:
            return
        self.datas.append(data)
 

    def output_html(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table border=1>')

        fout.write('<tr>')
        fout.write('<th style="width:%20">url</th>')
        fout.write('<th style="width:%10">title</th>')
        fout.write('<th style="width:%70">summary</th>')
        fout.write('</tr>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>') 
        fout.write('</html>')
        fout.close() 
