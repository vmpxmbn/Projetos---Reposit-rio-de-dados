import sqlite3
import os

class BibliotecaCRUD:
    def __init__(self):
        self.conn = sqlite3.connect('biblioteca.db')
        self.criar_tabelas()
    
    def criar_tabelas(self):
        cursor = self.conn.cursor()
        
        # Tabela de livros
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacao INTEGER,
                status TEXT DEFAULT 'disponivel'
            )
        ''')
        
        self.conn.commit()
        print("✅ Tabelas criadas com sucesso!")
    
    def adicionar_livro(self):
        print("\n📖 ADICIONAR NOVO LIVRO")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano de publicação: ")
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)",
            (titulo, autor, ano)
        )
        self.conn.commit()
        print("✅ Livro adicionado com sucesso!")
    
    def listar_livros(self):
        print("\n📚 TODOS OS LIVROS")
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        
        if not livros:
            print("📭 Nenhum livro cadastrado.")
            return
        
        for livro in livros:
            id, titulo, autor, ano, status = livro
            print(f"ID: {id} | {titulo} - {autor} ({ano}) | Status: {status}")
    
    def listar_livros_disponiveis(self):
        print("\n📚 LIVROS DISPONÍVEIS")
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE status = 'disponivel'")
        livros = cursor.fetchall()
        
        if not livros:
            print("📭 Nenhum livro disponível.")
            return
        
        for livro in livros:
            id, titulo, autor, ano, status = livro
            print(f"ID: {id} | {titulo} - {autor} ({ano})")
    
    def emprestar_livro(self):
        print("\n🎯 EMPRESTAR LIVRO")
        self.listar_livros_disponiveis()
        
        try:
            id_livro = int(input("\nID do livro para empréstimo: "))
            usuario = input("Nome do usuário: ")
            
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE livros SET status = 'emprestado' WHERE id = ? AND status = 'disponivel'",
                (id_livro,)
            )
            
            if cursor.rowcount > 0:
                print(f"✅ Livro emprestado para {usuario}!")
            else:
                print("❌ Livro não encontrado ou indisponível.")
            
            self.conn.commit()
            
        except ValueError:
            print("❌ ID deve ser um número!")
    
    def devolver_livro(self):
        print("\n🔄 DEVOLVER LIVRO")
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE status = 'emprestado'")
        livros_emprestados = cursor.fetchall()
        
        if not livros_emprestados:
            print("📭 Nenhum livro emprestado no momento.")
            return
        
        print("Livros emprestados:")
        for livro in livros_emprestados:
            id, titulo, autor, ano, status = livro
            print(f"ID: {id} | {titulo} - {autor}")
        
        try:
            id_livro = int(input("\nID do livro para devolução: "))
            
            cursor.execute(
                "UPDATE livros SET status = 'disponivel' WHERE id = ? AND status = 'emprestado'",
                (id_livro,)
            )
            
            if cursor.rowcount > 0:
                print("✅ Livro devolvido com sucesso!")
            else:
                print("❌ Livro não encontrado ou já disponível.")
            
            self.conn.commit()
            
        except ValueError:
            print("❌ ID deve ser um número!")
    
    def menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("📚 SISTEMA BIBLIOTECA - CRUD COMPLETO")
            print("="*50)
            print("1. 📖 Adicionar livro")
            print("2. 📚 Listar todos os livros")
            print("3. ✅ Listar livros disponíveis")
            print("4. 🎯 Emprestar livro")
            print("5. 🔄 Devolver livro")
            print("6. 🚪 Sair")
            print("="*50)
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.adicionar_livro()
            elif opcao == '2':
                self.listar_livros()
            elif opcao == '3':
                self.listar_livros_disponiveis()
            elif opcao == '4':
                self.emprestar_livro()
            elif opcao == '5':
                self.devolver_livro()
            elif opcao == '6':
                print("👋 Saindo do sistema...")
                break
            else:
                print("❌ Opção inválida!")
        
        self.conn.close()

# EXECUTAR O SISTEMA
if __name__ == "__main__":
    sistema = BibliotecaCRUD()
    sistema.menu_principal()