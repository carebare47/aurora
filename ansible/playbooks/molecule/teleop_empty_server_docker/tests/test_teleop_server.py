import os
import docker

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_docker_installed(host):
    package = host.package('docker-ce')
    assert package.is_installed


def test_docker_container_exists(host):
    client = docker.from_env()
    try:
        client.containers.get('dexterous_hand_real_hw')
        assert True
    except docker.errors.NotFound:
        assert False
    except docker.errors.APIError:
        assert False


def test_correct_docker_image(host):
    client = docker.from_env()
    image = str(client.containers.get('dexterous_hand_real_hw').image)
    assert image == "<Image: 'shadowrobot/dexterous-hand:kinetic-release'>"


def test_sr_config_exists_in_docker(host):
    client = docker.from_env()
    container = client.containers.get('dexterous_hand_real_hw')
    bits, stat = container.get_archive(
        '/home/user/projects/shadow_robot/base/src/sr_config')
    assert stat['size'] > 0


def test_icons_in_docker(host):
    f = host.file('/home/Desktop/Teleop_Launcher.desktop')
    assert f.exists
