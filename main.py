import database as db
import crud


BANNER = r"""
╔══════════════════════════════════════════════════════╗
║        SISTEMA DE INVENTÁRIO DE CIBERSEGURANÇA       ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""


def exibir_menu():
    print("""
┌─────────────────────────────────────────┐
│               MENU PRINCIPAL            │
├─────────────────────────────────────────┤
│  ATIVOS                                 │
│    1. Cadastrar ativo                   │
│    2. Buscar / listar ativo             │
│    3. Atualizar ativo                   │
│    4. Deletar ativo                     │
├─────────────────────────────────────────┤
│  VULNERABILIDADES                       │
│    5. Adicionar vulnerabilidade         │
│    6. Ver vulnerabilidades de um ativo  │
├─────────────────────────────────────────┤
│    0. Sair                              │
└─────────────────────────────────────────┘""")


def main():
    print(BANNER)
    db.inicializar_banco()


    ativos = db.carregar_em_dict()
    print(f"  Base carregada: {len(ativos)} ativo(s) no sistema.\n")

    ações = {
        "1": crud.cadastrar,
        "2": crud.buscar,
        "3": crud.atualizar,
        "4": crud.deletar,
        "5": crud.adicionar_vulnerabilidade,
        "6": crud.ver_vulnerabilidades,
    }

    while True:
        exibir_menu()
        opção = input("\n  Digite a opção: ").strip()

        if opção == "0":
            print("\n  Encerrando o sistema!\n")
            break

        ação = ações.get(opção)
        if ação:
            try:
                ação(ativos)
            except KeyboardInterrupt:
                print("\n  Operação cancelada pelo usuário.")
        else:
            print("  ✗ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
