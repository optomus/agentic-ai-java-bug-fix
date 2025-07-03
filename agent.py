# agent.py continued
from langchain import PromptTemplate, LLMChain
from github_tool import GitHubTool

# Load prompt
with open("fix_template.txt") as f:
    template = f.read()

prompt = PromptTemplate(
    input_variables=["filename", "code"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

# GitHub setup
gh_tool = GitHubTool(token="your_github_token")
code = gh_tool.get_file_content("youruser/yourrepo", "src/Calculator.java")

# Run reasoning chain
fix = chain.run({"filename": "Calculator.java", "code": code})

# Display or apply fix
print(f"Suggested Fix:\n{fix}")

# Optional: Submit PR
# pr_url = gh_tool.create_pr("youruser/yourrepo", "Bug Fix", "Fix null pointer bug", "bugfix-branch", "src/Calculator.java", fix)
# print(f"PR created: {pr_url}")
