from xml.dom import minidom



class ReusableTest:

    @classmethod
    def read_xml(cls, node_name):
        # parse an xml file by name
        my_doc = minidom.parse('/Users/mithunroy/PythonAppium/TestDataTable/inputdata.xml')
        # items = mydoc.getElementsByTagName('testdata')
        data = my_doc.getElementsByTagName(node_name)[0]
        return data.firstChild.data

    '''

    @staticmethod
    def generate_html_report(statustest):

        now = datetime.datetime.now()
        MM = now.strftime("%Y_%m_%d_%H_%M_%S")
        if statustest == "PASS":
            f = open(DataTable.HTMLReportPath() + 'Smoke_008_' + MM + '_PASS.html', 'w')
            message = """
                <html lang="en">
                <head>
                <style>
                body { background: #80d4ff; }
                </style>
                <meta charset="utf-8">
                </head>
                <body>""" \
                      + '<table border = "1"><tr style = "background-color: #9999ff"><th>'"Test Name"'</th><th>Smoke Test 008</th></tr>' + '</table>' \
                      + '<table border= "1"><tr style= "background-color: #C6EFCE"><td>SL No</td><td>Smoke Test Steps</td><td>Status</td></tr>' \
                      + '<tr style="background-color:#ffffcc"><td>1</td><td>' + \
                      'User can log in Successfully</td><td style="background-color:#00ff00">PASS</td></tr>' \
                      + '<tr style="background-color:#ffffcc"><td>2</td><td>' + \
                      'User Can add Past Order Successfully to Cart Page' + '</td><td style="background-color:#00ff00">PASS</td></tr>' \
                      + '<tr style="background-color:#ffffcc"><td>3</td><td>' + \
                      'Past Order added successfully to Cart Page' + '</td><td style="background-color:#00ff00">PASS</td></tr>' \
                      + '<tr style="background-color:#ffffcc"><td>4</td><td>' + \
                      'User Can Place Order Successfully with CASH-->' + ordernumber + '</td><td style="background-color:#00ff00">PASS</td></tr>' \
                      + """</body></html>"""
            f.write(message)
            f.close()
        else:
            f = open(DataTable.HTMLReportPath() + 'Smoke_008_' + MM + '_FAIL.html', 'w')
            message = """
                <html lang="en"><head><style>body { background: #ffffff; }</style><meta charset="utf-8"></head>
                <body><table border="1"><tr style="background-color:#ff5c33"><th>'"Smoke Test Name"'</th><th>Smoke Test 008 is RED</th></tr>'+'</table></body></html>"""
            f.write(message)
            f.close()
'''

    def another_html(self):

         with open('mypage.html', 'w') as HtmlFile:
            HtmlFile.write('<html>')
            HtmlFile.write('<body>')
            HtmlFile.write('<table>')
            HtmlFile.write('</table>')
            HtmlFile.write('</body>')
            HtmlFile.write('</html>')
            HtmlFile.close()

