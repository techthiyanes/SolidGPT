from solidgpt.orchestration.orchestration import *
from solidgpt.manager.gptmanager import GPTManager


def run_test():
    app = Orchestration()
    skill: WorkSkill = WritePRD()
    skill.init_config(
        [
            {
                "param_path": "in/ProductBasicInfo.json",
                "loading_method": "SkillInputLoadingMethod.LOAD_FROM_STRING",
                "load_from_output_id": -1
            },
        ],
        [
            {
                "id": 1
            }
        ])
    agent: WorkAgent = AgentSoftwareDeveloper(skill)
    node: WorkNode = WorkNode(0, agent)
    app.add_node(node)
    app.init_node_dependencies()
    app.save_data("config/config_data.json")
    app.execute()


def run_test_with_config():
    app = Orchestration()
    app.load_data("config/config_data.json")
    app.execute()


GPTManager()
run_test_with_config()