import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('painel')


# @pytest.fixture
# def resp_painel(client, db):
#     return client.get(reverse('base:painel'))
#
#
# def test_botao_entrar_disponivel(resp_painel):
#     assert_contains(resp_painel, 'Entrar')
