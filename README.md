# snaptutor
A simple app for providing feedback on textbook reflections. This demonstrates basic assessment qualities using GPT 3.5.

## How to use
The app is configured to run with Flask. If you have Python and Flask, you can clone this repository and run it using `flask run`.

The app takes user input and runs the result using OpenAI's Chat API. Users should select the textbook that the user is reflecting on using the radio buttons and then provide their reflection in the text box. The system is configured using the following query:

> Students will provide you with short reflections on emerging trends in the business world. Evaluate the reflections in terms of the following:
> - evidence of critical thought
> - proficiency with business or technology concepts
> Provide a written explanation of your evaluation that is between 10 and 50 words long. Conclude with an overall evaluation between 1 and 5 where 1 represents very poor performance and 5 represents excellent performance.

The site then writes ChatGPT's response in the space below the button.

## Sample reflections
Need some sample reflections? Consider copying and pasting the following to see ChatGPT's assessement.

### Stronger
> Thomson Reuters has a wide range of digital transformation products and is well-positioned to lead in this space. The  company has some of the leading real-time news sources, which has allowed them to develop advanced natural language processing tools, which they have tailored to professional services automation. They are likely to leverage this advantage, as there are few companies that have both the resources and capabilities to develop novel generative AI, due to the complexity of procuring and retaining vast quantities of novel data.

> I appreciated Walmart's implementation of sustainable practices. Their implementation of LED lighting and sustainable energy will likely have a measurable impact. I am not sure whether this is an example of greenwashing, though, because they provided their statistics in cumulative terms, rather than their annual emissions reductions.

### Weaker
> I think Thomson Reuters provides news. I don't really see how this makes them a technology leader.

> Walmart suuuuucks and its shares are gonna tank. Nobdy buys stuff from them.

## Problems
- The database has been configured but it doesn't do much with the textbook data. Ideally, the prompt would be refined to include the information about the textbook source.
- The prompt is still pretty general. It could use a fine-tuning feature to help it provide more consistent responses.

A huge shout out to the OpenAI Quickstart repository. The app is based on the quickstart tutorial. You can find it at https://github.com/openai/openai-quickstart-python
