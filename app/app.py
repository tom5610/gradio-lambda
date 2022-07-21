import gradio as gr
from mangum import Mangum

def greet(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text", allow_flagging="never")

app, _, _ = demo.launch(prevent_thread_lock=True)
handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    demo.block_thread()
