import os
import io
from PIL import Image
from flask import Flask, render_template, redirect, url_for
from toonify.fetcher import query
from toonify.input_form import InputForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/begin', methods=['POST', 'GET'])
def begin():
    form = InputForm()
    if form.validate_on_submit():
        prompts=[]
        prompt0 = form.prompt0.data
        prompts.append(prompt0)
        prompt1 = form.prompt1.data
        prompts.append(prompt1)
        prompt2 = form.prompt2.data
        prompts.append(prompt2)
        prompt3 = form.prompt3.data
        prompts.append(prompt3)
        prompt4 = form.prompt4.data
        prompts.append(prompt4)
        prompt5 = form.prompt5.data
        prompts.append(prompt5)
        prompt6 = form.prompt6.data
        prompts.append(prompt6)
        prompt7 = form.prompt7.data
        prompts.append(prompt7)
        prompt8 = form.prompt8.data
        prompts.append(prompt8)
        prompt9 = form.prompt9.data
        prompts.append(prompt9)

        print(prompts)

        return redirect(url_for('result', prompts = prompts))

    return render_template('generate.html', form=form)

@app.route('/result/<prompts>')
def result(prompts):
    # current_directory = os.getcwd()
    # child = 'toonify'
    # child_directory = os.path.join(current_directory, child)
    # TEMP_DIR = os.path.join(child_directory, 'static')
    # os.makedirs(TEMP_DIR, exist_ok=True)
    # prompt_list = prompts.split(',')
    # for i, prompt in enumerate(prompt_list):
    #     image_path = os.path.join(TEMP_DIR, f'image_{i}.png')
    #     raw_image = query({
	#     "inputs": prompt,
    #     })
    #     image = Image.open(io.BytesIO(raw_image))
    #     if os.path.exists(image_path):
    #         os.remove(image_path)
    #     image.save(image_path)
    return render_template('result.html')
