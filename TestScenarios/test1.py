import os
from pathlib import Path
from datetime import datetime


pro_path = Path(__file__).parent
print(pro_path)
x = str(pro_path).split("TestScenarios")[0]+str("TestReport/")
print(x)


class New_Class:



    def final_html(self):
            with open(x+'mypage.html', 'w') as HtmlFile:
                HtmlFile.write('<html style="background-color:powderblue;">')
                HtmlFile.write('<body padding-top: "100px";>')
                HtmlFile.write('<h1 align="center">Test Automation Report</h1>')
                HtmlFile.write('<p align="center">Date and Time :'+str(datetime.now())+'</p>')
                HtmlFile.write('<table align="center" border="1" bordercolor = "#003300"')
                HtmlFile.write('</table>')
                HtmlFile.write('<tr style="background-color:#ffe6ff">' +
                               '<th>Test Case ID</th>' +
                               '<th>Test Case Description</th>' +
                               '<th>Execution Status</th>' +
                               '</tr>')
                HtmlFile.write('</body>')
                HtmlFile.write('</html>')
                HtmlFile.close()

    def when_test_is_pass(html_string, test_id, test_desctiption):
        for x in range(10):
            html_string.write('<tr style="background-color:#f2f2f2">' +
           '<td>'+test_id+'</td>' +
           '<td>'+test_desctiption+'</td>' +
           '<td style="background-color:#b3ffcc">PASS</td>' +
           '</tr>')

    def when_test_is_fail(html_string, test_id, test_desctiption):
        for x in range(10):
            html_string.write('<tr style="background-color:#f2f2f2">' +
            '<td>' + test_id + '</td>' +
            '<td>' + test_desctiption + '</td>' +
           '<td style="background-color:#ffb3b3">FAIL</td>' +
           '</tr>')

