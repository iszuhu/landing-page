from flask import Flask

app = Flask(__name__)


@app.route("/iszu")
def hello_iszu():
    return"<h1> Welcome, Iszu! </h1>"


@app.route("/")
def hello_world():
    return """
<p>Hello, World!</p>
    <table><caption>Phone numbers</caption>
<thead>
<tr>
<th>Name</th>
<th colspan="2">Phone</th>
</tr>
</thead>
<tbody>
<tr>
<td>John</td>
<td>577854</td>
<td>577855</td>
</tr>
<tr>
<td>Jack</td>
<td>577856</td>
<td>577857</td>
</tr>
</tbody>
<tfoot>
<tr>
<td>&nbsp;</td>
<td>Personal</td>
<td>Office</td>
</tr>
</tfoot>
</table>"""