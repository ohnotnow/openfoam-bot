import os
from jinja2 import Template
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from responses import InvestigatorResponse, AdvisorResponse, WorkerResponse

def get_model(role: str):
    if role == 'investigator':
        return 'gpt-4o-mini'
    elif role == 'advisor':
        return 'gpt-4o-mini'
    elif role == 'worker':
        return 'gpt-4o-mini'
    else:
        raise ValueError(f"Unknown role: {role}")

def create_agent(role: str, model_name: str = ""):
    if not model_name:
        model_name = get_model(role)
    response_type = get_response_type(role)
    model = OpenAIModel(model_name)
    agent = Agent(model, result_type=response_type)
    return agent

def get_prompt(role: str, prompt_parameters: dict):
    try:
        with open(f'prompts/{role}.txt', 'r') as file:
            prompt_template = file.read()
    except FileNotFoundError:
        raise ValueError(f"Prompt file for role {role} not found")
    template = Template(prompt_template)
    return template.render(prompt_parameters)

def get_response_type(role: str):
    if role == 'investigator':
        return InvestigatorResponse
    elif role == 'advisor':
        return AdvisorResponse
    elif role == 'worker':
        return WorkerResponse
    else:
        raise ValueError(f"Unknown role: {role}")
