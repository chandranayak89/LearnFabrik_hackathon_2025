import click
import logging
from robot_controller import RobotController
from execution_engine import execute_workflow
import yaml

@click.command()
@click.option('--config', default='service_platform/config.yaml', help='Path to workflow config YAML')
@click.option('--robot-ip', default='192.168.2.14', help='Robot IP address')
@click.option('--robot-model', default='MAIRA', help='Robot model (MAIRA, LARA5, etc.)')
def run_workflow(config, robot_ip, robot_model):
    logging.basicConfig(level=logging.INFO)
    click.echo(f"Loading workflow from: {config}")
    with open(config, 'r') as f:
        workflow = yaml.safe_load(f)["workflow"]

    controller = RobotController(model=robot_model, ip=robot_ip)
    click.echo(f"Running workflow on {robot_model} at {robot_ip}...")
    execute_workflow(workflow, controller)
    click.echo("Workflow execution complete.")

if __name__ == "__main__":
    run_workflow()
