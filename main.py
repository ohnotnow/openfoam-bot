import re
from pydantic import BaseModel
from agents import create_agent, get_prompt
from responses import InvestigatorResponse, AdvisorResponse, WorkerResponse

def get_llm_response(role: str, prompt_parameters: dict) -> BaseModel:
    agent = create_agent(role)
    prompt = get_prompt(role, prompt_parameters)
    response = agent.run_sync(prompt)
    return response.data

def get_answer_to_questions(questions: list[str]) -> str:
    print("The agent has the following questions:")
    for question in questions:
        print(f"- {question}")
    answer = input("Your answer: ")
    answer = f"<user-answers-to-questions>{answer}</user-answers-to-questions>"
    return answer

def fix_llm_formatting(xml_string: str) -> str:
    xml_string = xml_string.replace('\\n', '\n')
    xml_string = re.sub(r'.+<file path=', '    <file path=', xml_string)
    return xml_string

def generate_simulation(project_description: str, requirements: str) -> str:
    investigator_response: InvestigatorResponse = get_llm_response('investigator', {
        'project_description': project_description,
        'requirements': requirements
    })

    if len(investigator_response.questions) > 0:
        answer = get_answer_to_questions(investigator_response.questions)
    else:
        answer = ""

    advisor_response: AdvisorResponse = get_llm_response('advisor', {
        'requirements': requirements,
        'answer': answer,
        'project_description': project_description,
        'specification': investigator_response
    })


    worker_response: WorkerResponse = get_llm_response('worker', {
        'requirements': requirements,
        'project_description': project_description,
        'specification': advisor_response
    })

    xml_string = fix_llm_formatting(worker_response.body)

    return xml_string

if __name__ == "__main__":
    project_description = input("Please describe your overall project (leave blank if n/a): ")
    requirements = input("Please describe your desired OpenFOAM simulation: ")

    xml_string = generate_simulation(project_description, requirements)
    print(xml_string)
