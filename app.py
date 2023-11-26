import gradio as gr
from sklearn.metrics import f1_score, precision_score, recall_score
import prometheus_client as prom
import joblib
import numpy as np
from fastapi import FastAPI, Request, Response

app = FastAPI()

f1_metric = prom.Gauge('healthprediction_f1_score', 'F1 score for random 100 test samples')

def update_metrics():
    test = test_data.sample(100)
    test_feat = test.iloc[:, :-1].values

    
    test_pred = my_model.predict(test_feat)
    f1 = f1_score(test_cnt, test_pred)

    f1_metric.set(f1)
    
myControls = {
    "ResultControl":None,
    "Feedback":None,
    "AdditionalInfo":None
}
def predict(imageToProcess):
    #myControls["ResultContro"].value = "No Disease"

    return ["No Disease", "Nothing is required"]

    
@app.get("/metrics")
async def get_metrics():
    update_metrics()
    return Response(media_type="text/plain", content= prom.generate_latest())

def submitFeedback(a,b):
    return ["User input submitted successfully"]

with gr.Blocks() as app :

    gr.Markdown(
    """
        # AI based plant Disease Detection Application
       
    """
    )
    imageInput = gr.Image()

    controls = []

    myControls["ResultControl"] = gr.Textbox(label='Possible Disease could be ')
    myControls["AdditionalInfo"] = gr.TextArea(label='Additional Info')
    controls.append(myControls["ResultControl"])
    controls.append(myControls["AdditionalInfo"])
    

    predictBtn = gr.Button(value='Predict')
    predictBtn.click(predict, inputs=imageInput, outputs=controls)


    gr.Markdown()
    myControls["Feedback"] = gr.Checkbox(label="Is prediction acceptable?")
    myControls["UserInput"] = gr.Textbox(label='What is the correct classification?')
    feedbackBtn = gr.Button(value='Submit Feedback')
    feedbackBtn.click(submitFeedback, inputs =[myControls["Feedback"], myControls["UserInput"]], outputs=None)




    app.launch()
app = gradio.mount_gradio_app(app, iface, path="/")	
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)   # Ref: https://www.gradio.app/docs/interface
