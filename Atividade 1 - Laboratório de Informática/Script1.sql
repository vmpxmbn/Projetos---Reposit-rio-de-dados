-- CONSULTA 1: LISTAR TODOS OS LIVROS DISPONÍVEIS
SELECT '=== LIVROS DISPONÍVEIS ===' AS '';
SELECT id, titulo, ano_publicacao, isbn 
FROM livros 
WHERE status = 'disponivel';

-- CONSULTA 2: ENCONTRAR LIVROS DE UM AUTOR ESPECÍFICO
SELECT '=== LIVROS DE MACHADO DE ASSIS ===' AS '';
SELECT l.titulo, l.ano_publicacao, l.status
FROM livros l
JOIN livros_autores la ON l.id = la.livro_id
JOIN autores a ON a.id = la.autor_id
WHERE a.nome = 'Machado de Assis';

-- CONSULTA 3: DETALHES COMPLETOS DOS LIVROS
SELECT '=== CATÁLOGO COMPLETO ===' AS '';
SELECT l.titulo, a.nome as autor, l.ano_publicacao, l.status
FROM livros l
JOIN livros_autores la ON l.id = la.livro_id
JOIN autores a ON a.id = la.autor_id
ORDER BY a.nome, l.titulo;
SHOW DATABASES;
USE biblioteca;
SHOW TABLES;