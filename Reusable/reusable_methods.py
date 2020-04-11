from xml.dom import minidom
from datetime import datetime



class ReusableTest:

    @classmethod
    def read_xml(cls, node_name):
        # parse an xml file by name
        my_doc = minidom.parse('/Users/mithunroy/PythonAppium/TestDataTable/inputdata.xml')
        # items = mydoc.getElementsByTagName('testdata')
        data = my_doc.getElementsByTagName(node_name)[0]
        return data.firstChild.data

    @classmethod
    def initial_html(cls, html_file, title):

        html_file.write('<html style="background-color:powderblue;">')
        html_file.write('<body padding-top: "100px";>')
        html_file.write('<h1 align="center">Test Automation Report: :'+title+'</h1>')
        html_file.write('<p align="center">Date and Time :' + str(datetime.now()) + '</p>')
        html_file.write('<table align="center" border="1" bordercolor = "#003300"')
        html_file.write('</table>')
        html_file.write('<tr style="background-color:#ffe6ff">' +
                       '<th><center>Test Case ID</center></th>' +
                       '<th><center>Test Case Description</center></th>' +
                       '<th><center>Execution Status</center></th>' +
                       '</tr>')

    @classmethod
    def final_html(cls, html_file):

        html_file.write('</body>')
        html_file.write('</html>')
        html_file.close()

    @classmethod
    def when_test_is_pass(cls, html_string, test_id, test_description):
        html_string.write('<tr style="background-color:#f2f2f2">'+
       '<td><center>'+test_id+'</center></td>' +
       '<td><center>'+test_description+'</center></td>' +
       '<td style="background-color:#b3ffcc"><center>PASS</center></td>' +
       '</tr>')

    @classmethod
    def when_test_is_fail(cls,html_string, test_id, test_description):
        html_string.write('<tr style="background-color:#f2f2f2">' +
        '<td><center>' + test_id + '</center></td>' +
        '<td><center>' + test_description + '</center></td>' +
       '<td style="background-color:#ffb3b3"><center>FAIL</center></td>' +
       '</tr>')

