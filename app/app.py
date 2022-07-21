import gradio as gr
from mangum import Mangum

def greet(name):
    return "Hello " + name + "!!"

# allow_flagging="never" is important 
# for AWS lambda as the default directory is not writable
# EFS will need to be setup for flagging to be 
# useful
demo = gr.Interface(fn=greet, inputs="text", outputs="text", allow_flagging="never")

app, _, _ = demo.launch(prevent_thread_lock=True)
handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    demo.block_thread()
