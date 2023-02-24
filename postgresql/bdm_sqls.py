'''
Trabalho de Banco de Dados Massivo
Queries para comparação de tempo com o MongoDB
'''



#########################################################
# PARTE 1 - DDLs
#########################################################

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Truncar tabela
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ddl_truncate_table = '''
    TRUNCATE TABLE ENEM_2021;
'''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Adicionar colunas à tabela - com comentários
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ddl_add_columns = '''
    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    ADD COLUMN NOTA_MEDIA_SIMPLES float8 null;
    COMMENT ON COLUMN "MPCA_BDM"."ENEM_2021".NOTA_MEDIA_SIMPLES IS 'Cálculo de media simples das 5 notas do ENEM';

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    ADD COLUMN NOTA_MEDIA_SIMPLES_QCAT float8 NULL;
    COMMENT ON COLUMN "MPCA_BDM"."ENEM_2021".NOTA_MEDIA_SIMPLES_QCAT IS 'Categoria das notas do ENEM';

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    ADD COLUMN ESCOLARIDADE_PAIS VARCHAR(50) NULL;
    COMMENT ON COLUMN "MPCA_BDM"."ENEM_2021".ESCOLARIDADE_PAIS IS 'Escolaridade dos pais - Guarda o que tem maior escolaridade';

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    ADD COLUMN ESCOLARIDADE_PAIS_DESC VARCHAR(500) NULL;
    COMMENT ON COLUMN "MPCA_BDM"."ENEM_2021".ESCOLARIDADE_PAIS_DESC IS 'Descrição da Escolaridade dos pais';

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    ADD COLUMN REGIAO VARCHAR(100) NULL;
    COMMENT ON COLUMN "MPCA_BDM"."ENEM_2021".REGIAO IS 'Região da UF';
    
    '''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Alterar nome de colunas
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ddl_rename_columns = '''
    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    RENAME COLUMN "Q001" TO ESCOLARIDADE_PAI;

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    RENAME COLUMN "Q002" TO ESCOLARIDADE_MAE;
 
    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    RENAME COLUMN "Q005" TO QTD_MORADORES_CASA;                             

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    RENAME COLUMN "Q006" TO RENDA_MENSAL_FAMILIA;    

    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    RENAME COLUMN "Q024" TO RESIDENCIA_COMPUTADOR;        
                              
    ALTER TABLE "MPCA_BDM"."ENEM_2021"  
    RENAME COLUMN "Q025" TO RESIDENCIA_INTERNET;   

    '''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# QUERIES
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# count
sql_select_count_total = '''
    select  count(*) 
    from  "MPCA_BDM"."ENEM_2021";
    '''
# select single row with WHERE
sql_select_single_row = '''
    select  *
    from  "MPCA_BDM"."ENEM_2021"
    where "NU_INSCRICAO" = @my_var;
    '''

# select all
sql_select_all = '''
    SELECT "NU_INSCRICAO"
    , "NU_ANO"
    , "TP_FAIXA_ETARIA"
    , "TP_SEXO"
    , "TP_ESTADO_CIVIL"
    , "TP_COR_RACA"
    , "TP_NACIONALIDADE"
    , "TP_ST_CONCLUSAO"
    , "TP_ANO_CONCLUIU"
    , "TP_ESCOLA"
    , "TP_ENSINO"
    , "IN_TREINEIRO"
    , "CO_MUNICIPIO_ESC"
    , "NO_MUNICIPIO_ESC"
    , "CO_UF_ESC"
    , "SG_UF_ESC"
    , "TP_DEPENDENCIA_ADM_ESC"
    , "TP_LOCALIZACAO_ESC"
    , "TP_SIT_FUNC_ESC"
    , "CO_MUNICIPIO_PROVA"
    , "NO_MUNICIPIO_PROVA"
    , "CO_UF_PROVA"
    , "SG_UF_PROVA"
    , "TP_PRESENCA_CN"
    , "TP_PRESENCA_CH"
    , "TP_PRESENCA_LC"
    , "TP_PRESENCA_MT"
    , "CO_PROVA_CN"
    , "CO_PROVA_CH"
    , "CO_PROVA_LC"
    , "CO_PROVA_MT"
    , "NU_NOTA_CN"
    , "NU_NOTA_CH"
    , "NU_NOTA_LC"
    , "NU_NOTA_MT"
    , "TX_RESPOSTAS_CN"
    , "TX_RESPOSTAS_CH"
    , "TX_RESPOSTAS_LC"
    , "TX_RESPOSTAS_MT"
    , "TP_LINGUA"
    , "TX_GABARITO_CN"
    , "TX_GABARITO_CH"
    , "TX_GABARITO_LC"
    , "TX_GABARITO_MT"
    , "TP_STATUS_REDACAO"
    , "NU_NOTA_COMP1"
    , "NU_NOTA_COMP2"
    , "NU_NOTA_COMP3"
    , "NU_NOTA_COMP4"
    , "NU_NOTA_COMP5"
    , "NU_NOTA_REDACAO"
    , "ESCOLARIDADE_PAI"
    , "ESCOLARIDADE_MAE"
    , "Q003"
    , "Q004"
    , "QTD_MORADORES_CASA"
    , "RENDA_MENSAL_FAMILIA"
    , "Q007"
    , "Q008"
    , "Q009"
    , "Q010"
    , "Q011"
    , "Q012"
    , "Q013"
    , "Q014"
    , "Q015"
    , "Q016"
    , "Q017"
    , "Q018"
    , "Q019"
    , "Q020"
    , "Q021"
    , "Q022"
    , "Q023"
    , "RESIDENCIA_COMPUTADOR"
    , "RESIDENCIA_INTERNET"
    FROM "MPCA_BDM"."ENEM_2021";
    '''
# select group by
sql_select_group_by = ''' 
    select residencia_computador, "NOTA_MEDIA_SIMPLES_QCAT",count(*)
    from "MPCA_BDM"."ENEM_2021"
    group by residencia_computador, "NOTA_MEDIA_SIMPLES_QCAT";
''' 

# select
sql_select_2 = '''
    select *
    from "MPCA_BDM"."ENEM_2021"
    where ("Q001" = 'F' or "Q001" = 'G'
    or "Q002" = 'F' or "Q002" = 'G')
    and "regiao" = 'SE'
    and "NU_NOTA_REDACAO" > 640

'''

sql_select_3 = '''
    select "Q001", "Q002", "Q024", count(*)
    from "MPCA_BDM"."ENEM_2021"
    group by "Q001", "Q002", "Q024"
    order by "Q001", "Q002", "Q024"

'''

sql_select_4 = '''
    select "regiao", count(*)
    from "MPCA_BDM"."ENEM_2021"
    group by "regiao"
    having count(*) > 200000
    order by "regiao"


'''

# delete
sql_delete_where_not_exists = ''' 
    delete from "MPCA_BDM"."ENEM_2021"
    where "TP_PRESENCA_CN" <> 1
        or "TP_PRESENCA_CH" <> 1
        or "TP_PRESENCA_LC" <> 1
        or "TP_PRESENCA_MT" <> 1
        or "TP_STATUS_REDACAO" <> 1
    '''
#delete from "MPCA_BDM"."ENEM_2021" 
#    where "TP_PRESENCA_CN" <> 1
#        or   des."TP_PRESENCA_CH" <> 1
#        or   des."TP_PRESENCA_LC" <> 1
#        or   des."TP_PRESENCA_MT" <> 1
    

# update - cálculo da média
sql_update_media_simples = ''' 
    update "MPCA_BDM"."ENEM_2021"
    set NOTA_MEDIA_SIMPLES  = ("NU_NOTA_LC" + "NU_NOTA_CH" + "NU_NOTA_CN" + "NU_NOTA_MT" + "NU_NOTA_REDACAO")/5;
    '''

# update - região
sql_update_regiao_prova = ''' 
    update "MPCA_BDM"."ENEM_2021"
    set "regiao"  = @var_regiao
    where "SG_UF_PROVA" in (@var_ufs)
    '''

