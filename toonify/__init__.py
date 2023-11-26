import io
from PIL import Image
from flask import Flask, render_template, redirect, url_for
from toonify.fetcher import query
from toonify.input_form import InputForm

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        prompts=[]
        prompt0 = form.promt0.data
        prompts.append(prompt0)
        prompt1 = form.promt1.data
        prompts.append(prompt1)
        prompt2 = form.promt2.data
        prompts.append(prompt2)
        prompt3 = form.promt3.data
        prompts.append(prompt3)
        prompt4 = form.promt4.data
        prompts.append(prompt4)
        prompt5 = form.promt5.data
        prompts.append(prompt5)
        prompt6 = form.promt6.data
        prompts.append(prompt6)
        prompt7 = form.promt7.data
        prompts.append(prompt7)
        prompt8 = form.promt8.data
        prompts.append(prompt8)
        prompt9 = form.promt9.data
        prompts.append(prompt9)

        return redirect(url_for('result', prompts = prompts))

    return render_template('index.html')

@app.route('/result')
def result(prompts):
    image_collection = []
    for prompt in prompts:
        raw_image = query({
	    "inputs": prompt,
        })
        encoded_image = base64.b64encode(raw_image).decode('utf-8')
        image_collection.append(encoded_image)

    return render_template('result.html', image_collection = image_collection)
