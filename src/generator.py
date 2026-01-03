from transformers import pipeline



def format( text) -> str:
    system_message = f"You are an expert in writing novels. You have won many prices."
    user_message = f"Please assist based on the following context: {text}"
    prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_message}<|eot_id|>" 
    prompt += f"<|start_header_id|>user<|end_header_id|>\n\n{user_message}<|eot_id|>"
    prompt += "<|start_header_id|>assistant<|end_header_id|>\n\n"
    return prompt
        
def generate(text, the_model, max_length, temperature, repetition_penalty):
    print(text)
    text = format(text)
    generator = pipeline("text-generation", model=the_model)
    result = generator(
        text,
        num_return_sequences=1,
        max_length=max_length,
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        no_repeat_ngram_size=2,
        early_stopping=False,
    )
    return result[0]["generated_text"]


def complete_with_gpt(
    text, context, the_model, max_length, temperature, repetition_penalty
):
    # Use the last [context] characters of the text as context
    max_length = max_length + context
    return generate(
        text[-context:], the_model, max_length, temperature, repetition_penalty
    )


# complete_with_gpt("I am a language model",200,'gpt2-medium',1500,0.7,1.5)
# def generate(genre:str,topic:str,main_name:str,type_of_main_character:str,antagonist_name:str,
#              antagonist_type:str,supporting_character_name:str,supporting_char_type:str,settings:str,
#              resoluton:str,chapter:int
#              ):
#     chapter_text={}
#     for x in range(chapter):0
