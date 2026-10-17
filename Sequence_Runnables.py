prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words")

model = Chatai(model = gemini, temperature=0.7)

parser = StrOutputParser()

chain = prompt | model | parser

chain.invoke() 