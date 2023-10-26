from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/<int:num>/<int:num2>')         
def repeat_word(num, num2):
    return render_template ("index.html", num=num, num2=num2)

    
    




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  


    