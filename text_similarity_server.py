import hug
import text_similarity as ts

@hug.post(
    "/",
)
def text_similarity(
    text1: hug.types.text,
    text2: hug.types.text
):
    return ts.text_similarity(text1, text2)
