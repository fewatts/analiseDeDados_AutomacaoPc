#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int opcao = 0;
char nome[100];
char cep[15];

void TelaLogin(){

    char login[15] = "teste";
    char login1[15];
    char senha[15] = "123";
    char senha1[15];        
    int login_efetuado = 0; 

    while(!login_efetuado){
    	
        printf("******SISTEMA DE DIAGNOSTICO DE COMORBIDADES COVID-19******\n\n");
        printf("Fazer o Login abaixo:\n\n");
		printf("Digite o Usuario: ");
        scanf("%s", login1);

        printf("Digite a Senha: ");
        scanf("%s", senha1);

        if (strcmp(login, login1) == 0 && strcmp(senha, senha1) == 0){
        	
        	system("cls");
            printf("********VOCE ESTA LOGADO!********\n\n");
            login_efetuado = 1;
        }
        else
            printf("\n\nDADOS INVALIDOS!\n\n");    
    }

}


void MostrarMenu(){

    printf("1) - CADASTRO DE PACIENTES\n");
    printf("2) - VERIFICAR GRUPO DE RISCO\n");
    printf("3) - SAIR DO SISTEMA\n\n");    
    printf("DIGITE UMA OPCAO: ");
    scanf("%d", &opcao);
    
	printf("\n\n");
	
    getchar();    

}

void CadastroPacientes(){
	
	printf("***********************************************\n");
    printf("ADICIONE OS DADOS DO PACIENTE!\n\n");
    
    char nome[100];
    char cpf[20];
    char telefone[31];
    char ruaenumero[51];
    char bairro[21];
    char cidadeeestado[41];
    char cep[15];
    int dia, mes, ano;
    char email[30];
    int diad, mesd, anod;
    int idade;
    FILE *cadastro;
    FILE *grupo_risco;
	
	
    int opcao = 0, count = 1, op = 2; 

    do{
        cadastro = fopen("Cadastro.txt", "a");
		
		
		
        if(cadastro == NULL){
        	
            printf("ERRO NA ABERTURA DO ARQUIVO");
            break;
            
        }else{
        	
            printf("\nCadastro %d\n\n", count);  			  
			           
            while(op == 2){
            	
                fflush(stdin);
				printf("Nome paciente: \n");
                scanf("%99[^\n]s", nome);
                printf("O nome digitado foi: %s\n", nome);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);  
				fflush(stdin);                             
			}
            
            	op = 2;	
                                  
            fprintf(cadastro, "%s\n", nome);          
                     
                        
            while(op == 2){
            	
                printf("\nCPF paciente: \n");
                scanf("%s", cpf);
                printf("O cpf digitado foi: %s\n", cpf);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin);                
			}
				
                op = 2;		
                                       
            fprintf(cadastro, "CPF: %s\n", cpf);           
                        
            
            while(op == 2){
            	
                printf("\nTelefone paciente: \n");
                scanf("%30[^\n]s", telefone);
                printf("O telefone digitado foi: %s\n", telefone);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin); 
            }
                
                op = 2;	        
                        
            fprintf(cadastro, "Telefone: %s\n", telefone);           
                                               

            while(op == 2){
            	
                printf("\nRua e numero paciente:\n ");                   
                scanf("%50[^\n]s", ruaenumero);				
                printf("\nA rua digitada foi: %s\n", ruaenumero);                 
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);                
                fflush(stdin); 
			}
				
            	op = 2;	            
                       
            fprintf(cadastro, "Rua e numero: %s\n", ruaenumero);
                                    

            while(op == 2){
            	
                printf("\nBairro paciente: \n");
                scanf("%20[^\n]s", bairro);
                printf("\nO bairro digitado foi: %s\n", bairro);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin);                 
			}
				
            	op = 2;	                     
            
            fprintf(cadastro, "Bairro: %s\n", bairro);            
                        
            
            while(op == 2){
            	
                printf("\nCidade e estado [cidade-estado]: \n");
                scanf("%40[^\n]s", cidadeeestado);
                printf("\nA informacao digitada foi: %s\n", cidadeeestado);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin); 
            }
                
            	op = 2;	
                                  
            fprintf(cadastro, "Cidade e estado: %s\n", cidadeeestado);          
                                               

            while(op == 2){
            	
                printf("\nCEP paciente: \n");
                scanf("%15[^\n]s", cep);
                printf("O cep digitado foi: %s\n", cep);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin); 
			}
				
            	op = 2;	
                   
            fprintf(cadastro, "CEP: %s\n", cep);
                                    
            
            while(op == 2){
            	
                printf("\nData de nascimento paciente: \n");
                printf("Dia: \n");
                scanf("%d", &dia);
                printf("Mes: \n");
                scanf("%d", &mes);
                printf("Ano: \n");
                scanf("%d", &ano);
                printf("\nA data digitada foi: %d/%d/%d\n", dia, mes, ano);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%d", &op);
                fflush(stdin);                 
			}
				
            	op = 2;	
                                   
            fprintf(cadastro, "Data de nascimento: %d/%d/%d\n", dia, mes, ano);           
                                                

            while(op == 2){
            	
                printf("\nE-mail: \n");
                scanf("%30[^\n]s", email);
                printf("O email digitado foi: %s\n", email);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin);                 
			}
            	op = 2;	
                            
            fprintf(cadastro, "E-mail: %s\n", email);                                    
                      

            while(op == 2){
            	
                printf("\nData de diagnostico paciente: \n");
                printf("Dia: \n");
                scanf("%d", &diad);
                printf("Mes: \n");
                scanf("%d", &mesd);
                printf("Ano: \n");
                scanf("%d", &anod);
                printf("\nA data digitada foi: %d/%d/%d\n", diad, mesd, anod);
                printf("\nConfirma esse dado?\n[1-sim] [2-nao]\n");
                scanf("%i", &op);
                fflush(stdin);                 
			}
				
            	op = 2;	                    
            
            	fprintf(cadastro, "Data do diagnostico: %d/%d/%d\n", diad, mesd, anod);
            	fprintf(cadastro, "************************************************\n");
            	
			idade=(anod-ano);

			if (idade >= 65){
				
				printf("\n\nO PACIENTE %s TEM: %d ANOS DE IDADE E PERTENCE AO GRUPO DE RISCO\n", nome, idade);
				grupo_risco = fopen("grupo_risco.txt", "a");
				fprintf(grupo_risco, "O PACIENTE %sTEM: %d ANOS DE IDADE E PERTENCE AO GRUPO DE RISCO\n", nome, idade);
				cadastro = fopen("Cadastro.txt", "a");
				fprintf(grupo_risco, "CEP: %s\n", cep);
				fflush(stdin); 
				
			}else{
				
			printf("\nO PACIENTE %s TEM: %d ANOS DE IDADE E NAO PERTENCE AO GRUPO DE RISCO\n", nome, idade);
				fflush(stdin); 
			
			}
			
		
            printf("\n****TODOS OS DADOS DE %s FORAM SALVOS COM SUCESSO!******\n\n", nome);
			printf("********************FIM DO CADASTRO*******************\n");
           
            fclose(cadastro);

            printf("\n\n[1-parar]\n[0-continuar]\n");
            
            scanf("%d", &opcao);
            
            count++;
		}
	}
    
    while(opcao != 1);
    
     
	     exit(0);   
        //getchar(); 
 
	 	
	 
	
	 
	 
	    
}



void VerificaGrupoRisco(){
	
	printf("*********************\n");
    printf("***VERIFICAR SE PACIENTE PERTENCE AO GRUPO DE RISCO!***\n\n");
    
    int i;
	int comorbidade;
	int voltar;
	
	FILE *cadastro;
	FILE *grupo_risco;
	
	grupo_risco = fopen("grupo_risco.txt", "a");
	cadastro = fopen("Cadastro.txt", "r");
	
		if(grupo_risco == NULL)
	{
		printf("Erro na abertura do arquivo!");
		}
	
	
	printf("POSSUI ALGUMA COMORBIDADE? [0 - NAO] / [1 - SIM]\n");
	scanf("%i", &comorbidade);
	
	if (comorbidade == 0){
		
		printf("\nOK!\n\n");
		printf("DESEJA VOLTAR A TELA INICIAL? [0 - NAO] / [1 - SIM]\n\n");
		scanf("%i", &voltar);
		
		if (voltar == 1){
			
			system("cls");
			printf("********VOCE ESTA LOGADO!********\n\n");
			
			MostrarMenu();
			
			switch (opcao)

        {

            case 1 : 

                CadastroPacientes();

            break;

            case 2 : 

                VerificaGrupoRisco();

            break;

			case 3 :
				
				printf("\n\n*********************\n");
				printf("*****LOG OFF REALIZADO COM SUCESSO!******\n");
				printf("*********************\n\n");
				exit(0);
												
            default :

                printf("Opção Invalida!");

            break;    
        }

        getchar();
			
			
			
		}else
		
		exit(0);
		
	}
			
	else if (comorbidade == 1)
	{
		
	printf("\n*********************");		
	printf("\nDIGITE O NUMERO REFERENTE A COMORBIDADE:\n\n1 - DIABETES\n2 - OBESIDADE\n3 - HIPERTENSAO\n4 - TUBERCULOSE\n5 - OUTROS\n6 - VOLTAR\n\n");
	printf("Numero: ");
	scanf("%i", &i);
	
		switch (i){
			
			case 1:
				grupo_risco = fopen("grupo_risco.txt", "a");
				fprintf(grupo_risco, "TIPO DE COMORBIDADE: [%i] - Diabetes.\n", i);	
				fprintf(grupo_risco, "**********************************************************");						
				fclose(grupo_risco);
				printf("\nSalvo em arquivo com sucesso!\n");
				break;
				
			case 2:
				
				grupo_risco = fopen("grupo_risco.txt", "a");
				fprintf(grupo_risco, "TIPO DE COMORBIDADE: [%i] - Obesidade.\n", i);	
				fprintf(grupo_risco, "**********************************************************");						
				fclose(grupo_risco);
				printf("\nSalvo em arquivo com sucesso!\n");
				break;
				
			case 3:
				
				grupo_risco = fopen("grupo_risco.txt", "a");
				fprintf(grupo_risco, "TIPO DE COMORBIDADE: [%i] - Hipertensao.\n", i);	
				fprintf(grupo_risco, "**********************************************************");						
				fclose(grupo_risco);
				printf("\nSalvo em arquivo com sucesso!\n");
				break;
				
			case 4:
				
				grupo_risco = fopen("grupo_risco.txt", "a");
				fprintf(grupo_risco, "TIPO DE COMORBIDADE: [%i] - Tubersulose.\n", i);	
				fprintf(grupo_risco, "**********************************************************");						
				fclose(grupo_risco);
				printf("\nSalvo em arquivo com sucesso!\n");
				break;
				
			case 5:
				
				grupo_risco = fopen("grupo_risco.txt", "a");
				fprintf(grupo_risco, "TIPO DE COMORBIDADE: [%i] - Outros tipos de Comorbidade.\n", i);	
				fprintf(grupo_risco, "**********************************************************");						
				fclose(grupo_risco);
				printf("\nSalvo em arquivo com sucesso!\n");
				break;
				
			case 6:
				
				system("cls");
				printf("********VOCE ESTA LOGADO!********\n\n");
			
				MostrarMenu();
			
			switch (opcao)

        {

            case 1 : 

                CadastroPacientes();

            break;

            case 2 : 

                VerificaGrupoRisco();

            break;

			case 3 :
				
				printf("\n\n*********************\n");
				printf("*****LOG OFF REALIZADO COM SUCESSO!******\n");
				printf("*********************\n\n");
				exit(0);
												
            default :

                printf("Opção Invalida!");

            break;    
        }

        getchar();
				
			default:
				
				printf("\nOpcao nao valida!\n");
				printf("Digite um numero entre 1 e 6!");
				break;
		}
	}
			
	else
	
	printf("\nDigite apenas 0 ou 1!\n");
	system("pause");	
    
     
}


int main(void){
	
	

    TelaLogin();

    MostrarMenu();

        switch (opcao)

        {

            case 1 : 

                CadastroPacientes();

            break;

            case 2 : 

                VerificaGrupoRisco();

            break;

			case 3 :
				
				printf("\n\n*********************\n");
				printf("*****LOG OFF REALIZADO COM SUCESSO!******\n");
				printf("*********************\n\n");
				exit(0);
												
            default :

                printf("Opção Invalida!");

            break;    
        }

        getchar(); 


    return (0);
	
}