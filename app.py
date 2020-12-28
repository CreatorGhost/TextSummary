from flask import Flask, render_template ,request
import model
import webScrap
app = Flask(__name__)



@app.route('/')
def hello():
    return render_template("summry.html")

@app.route('/summarize',methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        data = request.form.to_dict()
        if 'test' in data:
            print(data['test'])
            text=model.generate_summary(data['test'])
            return render_template('summry.html', my_string=text) 
        else:
            print(data['web'])
            text=webScrap.getUrl(data['web'])
            text=model.generate_summary(text)
            return render_template('summry.html', my_string=text) 
    else:
        return f"Something Not Right "
    






#model.generate_summary(post)


if __name__ == '__main__':
    app.run()