import os
import io
import requests
from PIL import Image
from flask import Flask, render_template, redirect, url_for, request
from toonify.fetcher import query
from toonify.input_form import InputForm
from dotenv import load_dotenv

load_dotenv()

SECRETKEY = os.getenv("SECRETKEY")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRETKEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/begin', methods=['POST', 'GET'])
def begin():
    form = InputForm()
    if form.validate_on_submit():
        prompts=[]
        #####
        if form.annot0.data:
            prompt0 = form.prompt0.data + " with empty speech bubble"
        else:
            prompt0 = form.prompt0.data + " wthout any speech bubbles"
        prompts.append(prompt0)
        ######
        if form.annot1.data:
            prompt1 = form.prompt1.data + " with empty speech bubble"
        else:
            prompt1 = form.prompt1.data + " wthout any speech bubbles"
        prompts.append(prompt1)
        ######
        if form.annot2.data:
            prompt2 = form.prompt2.data + " with empty speech bubble"
        else:
            prompt2 = form.prompt2.data + " wthout any speech bubbles"

        prompts.append(prompt2)
        ######
        if form.annot3.data:
            prompt3 = form.prompt3.data + " with empty speech bubble"
        else:
            prompt3 = form.prompt3.data + " wthout any speech bubbles"
        prompts.append(prompt3)
        ######
        if form.annot4.data:
            prompt4 = form.prompt4.data + " with empty speech bubble"
        else:
            prompt4 = form.prompt4.data + " wthout any speech bubbles"
        prompts.append(prompt4)
        ######
        if form.annot5.data:
            prompt5 = form.prompt5.data + " with empty speech bubble"
        else:
            prompt5 = form.prompt5.data + " wthout any speech bubbles"
        prompts.append(prompt5)
        ######
        if form.annot6.data:
            prompt6 = form.prompt6.data + " with empty speech bubble"
        else:
            prompt6 = form.prompt6.data + " wthout any speech bubbles"
        prompts.append(prompt6)
        ######
        if form.annot7.data:
            prompt7 = form.prompt7.data + " with empty speech bubble"
        else:
            prompt7 = form.prompt7.data + " wthout any speech bubbles"
        prompts.append(prompt7)
        ######
        if form.annot8.data:
            prompt8 = form.prompt8.data + " with empty speech bubble"
        else:
            prompt8 = form.prompt8.data + " wthout any speech bubbles"
        prompts.append(prompt8)
        ######
        if form.annot9.data:
            prompt9 = form.prompt9.data + " with empty speech bubble"
        else:
            prompt9 = form.prompt9.data + " wthout any speech bubbles"
        prompts.append(prompt9)
        ######

        return redirect(url_for('result', prompts = prompts))

    return render_template('generate.html', form=form)

@app.route('/result/<prompts>')
def result(prompts):
    current_directory = os.getcwd()
    child = 'toonify'
    child_directory = os.path.join(current_directory, child)
    TEMP_DIR = os.path.join(child_directory, 'static')
    os.makedirs(TEMP_DIR, exist_ok=True)
    prompt_list = prompts.split(',')
    for i, prompt in enumerate(prompt_list):
        image_path = os.path.join(TEMP_DIR, f'image_{i}.png')
        prompt+= "with a speech bubble"
        raw_image = query({
	    "inputs": prompt,
        })
        image = Image.open(io.BytesIO(raw_image))
        if os.path.exists(image_path):
            os.remove(image_path)
        image.save(image_path)
    return render_template('result.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.get('feedback')
    if feedback:
        current_directory = os.getcwd()
        child_directory = os.path.join(current_directory, 'toonify')
        logs_directory = os.path.join(child_directory, 'logs')
        feedback_file_path = os.path.join(logs_directory, 'feedback.txt')
        with open(feedback_file_path, 'a') as file:
            file.write(feedback + '\n')
    return redirect(url_for('index'))

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html'), 404
