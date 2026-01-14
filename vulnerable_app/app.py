from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Search Page</h2>
<form method="get">
  <input name="q">
  <input type="submit">
</form>
<p>Result: {{ result }}</p>
"""

@app.route("/", methods=["GET"])
def search():
    q = request.args.get("q", "")
    return render_template_string(HTML, result=q)

if __name__ == "__main__":
    app.run(debug=True)
