from decoracao.rest.rest_conf import criar_aplicacao_fastapi


def main():
    app = criar_aplicacao_fastapi()
    return app


if __name__ == '__main__':
    main()
