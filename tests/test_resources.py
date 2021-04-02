def test_get_ackermann(client, mocker):
    mocker.patch('main.ackermann', return_value=3)
    q = 'm=1&n=1'
    response = client.get(f'/ackermann?{q}')

    assert response.status_code == 200
    assert response.json() == {'result': str(3)}


def test_get_fibonacci(client, mocker):
    mocker.patch('main.fibonacci', return_value=2)
    q = 'n=3'
    response = client.get(f'/fibonacci?{q}')

    assert response.status_code == 200
    assert response.json() == {'result': str(2)}


def test_get_factorial(client, mocker):
    mocker.patch('main.factorial', return_value=1)
    q = 'n=1'
    response = client.get(f'/factorial?{q}')

    assert response.status_code == 200
    assert response.json() == {'result': str(1)}
