/*resete tabela */
TRUNCATE TABLE NAMETB;

/*fala para eu usar a dabese*/
USE NOMEBANCO;

/*criação de tabela*/
CREATE TABLE NAMETB(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    /*NOMECOLUNA TIPO(PARAMETRO) RESTRIÇÃO(NOT NULL/ UNIQUE)*/
    NOME VARCHAR(120) NOT NULL,
    EMAIL VARCHAR(120) UNIQUE,
    SENHA VARCHAR(255)
);

/*deleta uma tabela do banco*/
DROP TABLE NAMETB;

/*criar um banco de dados
    não fuciona no sharecloud*/
CREATE DATABASE test;


/*ver se a tabela(mesmo vale para ) USERS já exite
    caso ela existe o slq não cria uma databe*/
CREATE TABLE IF NOT EXISTS USERS (id INT);

/*para inserir na tabela*/
INSERT INTO tabela (ID) 
    VALUES (2),
    /*a linha a baixo sera add tambem na table*/
    (2245678);

/*funçõa: */
/*gere a data atual*/
NOW(); /*ou a func: ->*/ CURRENT_TIMESTAMP();

/*add o uma coluna na tabela*/
ALTER TABLE tabla ADD coluna typo;

/*filtra o jeito qs dados são mostrados*/
SELECT Colun¹, Colun² FROM tabala WHERE Coluna* condition;
/*Á "Colun²" é o picional;
 * = siginifica para pega todas as colunas;
 WHERE é opicional;
 Couna* = para fazer o filtro de qual linha vc vai procura á "codtion" ajuda a fazer a filtragem melhor;
    COUNT(): Conta o número de linhas. 
    AVG(): Calcula o valor médio. 
    SUM(): Calcula a soma de uma coluna. 
    MIN(): Encontra o menor valor de uma coluna. 
    MAX(): Encontra o maior valor de uma coluna     
*/

/*altualização o dado da linha*/
UPDATE tabela SET coluna = dato WHERE coluna* coditon;

/*deleta a linha*/
DELETE FROM tabela WHERE coluna* coditon 

/*tipo de var:*/
    SMALLINT => INTEGER/INT só que ocupa metado da moria do banco
    NUMERIC(255) => número com . ou negativos
    DECIAMAL => tem mas precição apos a virgula (depende do banco)
    REAL => valores com virgulas só que amarzenada em potencia
    BIT => 1/0
    BIT VARYING(225) => con junto maior de bit, muito usado para slavar imagemns
    DATE => datas
    TIME => add horas
    TIMESTAMP = > faz o que o date e o time faz só que juntos
    VARCHAR => txt
    INTERVAL => intervalo de tempo



CREATE TABLE tabela (
    id INTEGER NOT NULL
    id_outer_table INTEGER

    VARCHAR_com_DEFAULT VARCHAR(255) DEFAULT "sou o default" => isso carente casso ele não seja passada ná hora de add uma linha ela add o DEFAULT
    SEXO CHAR(1) CHECK ( UPPER(SEXO) == "M" OR UPPER(SEXO) = "F") => isso vala qual valores poden entra ou seja só M ou F


    FOREIGN KEY id_outer_table (id) REFERENCES table² (id_table²)
    /* id_outer_table => opicional
        table² = onde está a chave primaria ná outra tabela*/
    ON UPDATE ação
    ON DELETE ação
    /*açãoes: */
        SET NULL => deixa a coluna dessa tabela com NULL
        SET DEFAULT => altera para o DEFAULT dessa coluna se ouver
        CASCADE => exclui ou atualiza o resgistro que tem aver com chave
        NO ACTION => não faz nada
        RESTRICT => não exclua chave primaria 
);

/*modifica colunas:*/
ALTER TABLE tabela MODIFY (coluna tipoDado CONTION-caso_tenha)

/*excluir elemntos: */
ALTER TABLE tabela DELETE colun² CONTION

/*renomeação de nome: */
ALTER TABLE tabela RENAME nome-table => altera o nome da tabela 

ALTER TABLE tabala RENAME coluna_velha TO coluna_nova => altera o nome da coluna
