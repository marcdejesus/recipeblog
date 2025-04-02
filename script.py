from openai import OpenAI

client = OpenAI()

user_profile = {
  "dietary_restrictions":"salmon, perch, tuna, dairy, wheat",
  "cuisine_preferences":"mediterranean, japanese, puerto rican, italian",
  "ingredients_available":"chicken, eggs, quick steak, rice, beans, mushrooms, butter, olive oil, marinara sauce, penne, ground turkey, tomatoes, all table seasonings, onion, heavy cream"
}

system_prompt = {
  "role":"system",
  "content":"Generate an HTML code for a recipe blog that considers dietary restrictions, cuisine type, and ingredients."
}

restrictions = user_profile.get("dietary_restrictions")
preferences = user_profile.get("cuisine_preferences")
ingredients = user_profile.get("ingredients_available")

user_content1 = f'I want to create a recipe blog post. Here are my dietary restrictions: {restrictions}. My cuisine preferences include: {preferences}. The ingredients I have available are: {ingredients}.'

user_content2 = "Please provide a blog post with a title, description, ingredients, and instructions. Format the ingredients and instructions as follows: Ingredients should be bulleted, and instructions should be numbered."

user_content3 = "The recipe must use only the listed ingredients and should result in a single blog post with instructions not exceeding six steps."

user_prompt = {
  "role":"user",
  "content": user_content1 + "\n" + user_content2 + "\n" + user_content3
}

response = client.chat.completions.create(
  model="gpt-3.5-turbo", 
  messages=[user_prompt]
)

print(response.choices[0].message.content)
