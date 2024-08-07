import google.generativeai as genai

## function to load Gemeni Pro model and get responses
model=genai.GenerativeModel('gemini-1.5-flash-latest')
def get_gemini_response (input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# method to update a model
def input_image_details(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

