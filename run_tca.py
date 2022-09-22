import yaml
import json
from service.assessment import Assessment
from service.planning import Plan
from service.infer_tech import InferTech

plan = Plan()

with open('cfservices-32194c9906854947.yaml') as file:
    obj = yaml.safe_load(file)

    for o in obj['spec']['services']:
        print(o['servicebrokername'])

        input = [
          {
            "application_name": o['label'],
            "application_description": o['description'],
            "component_name": "",
            "operating_system": "",
            "programming_languages": "",
            "middleware": "",
            "database": "",
            "integration_services_and_additional_softwares": "",
            "technology_summary": o['servicebrokername']
          }
        ]

        assessment = Assessment()
        assess_result = assessment.app_validation(input)

        print(json.dumps(assess_result, indent=2))

        plan_result = plan.ui_to_input_assessment(assess_result)

        print(json.dumps(plan_result, indent=2))

        print('-------------------')
