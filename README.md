# Instagram Comment Scraper 🕷️

## Sobre o Projeto 🔎
Este projeto foi desenvolvido com fins educacionais para estudar conceitos de **Web Scraping** e a integração com a plataforma **Apify**.

O objetivo principal não é ser um produto final, mas sim demonstrar como estruturar uma aplicação Python robusta que consome dados externos, valida entradas "sujas" e expõe os resultados via API.

## Funcionalidades 🖥️
- **Extração de Dados:** Coleta comentários de publicações do Instagram (Reels ou Fotos) utilizando *Actors* da Apify.
- **Validação e Limpeza:** Converte dados brutos JSON em objetos Python estruturados usando **Pydantic**.
- **Filtragem:** Capacidade de filtrar comentários por palavras-chave específicas.
- **Tratamento de Erros:** Gestão de falhas de API e dados vazios com exceções personalizadas.

## Tecnologias Utilizadas 👨‍💻
- **Python 3.12+**
- **FastAPI:** Framework para construção da API REST.
- **Apify Client:** SDK para comunicação com os robôs de scraping.
- **Pydantic:** Para modelagem de dados (Schemas) e validação.
- **Poetry:** Gerenciamento de dependências e ambiente virtual.

## Arquitetura Simplificada 🧱
O código foi organizado seguindo o princípio de separação de responsabilidades:

1. **Routes (Controller):** Recebe a requisição HTTP e valida os parâmetros.
2. **Service:** Contém a regra de negócio (ex: lógica de filtragem por keyword).
3. **Client:** Responsável puramente pela comunicação externa com a Apify.
4. **Schemas:** Define a estrutura dos dados e realiza a conversão (DTOs inteligentes).

## Configuração ⚙️
Para funcionar, o projeto necessita de um arquivo `.env` na raiz contendo o token de acesso:

```env
APIFY_TOKEN=seu_token_da_apify_aqui
```

Para informações mais concisas e possibilidade de acesso ao TOKEN da API consulte o site oficial da APIFY: 
```https://apify.com/``` ou ```https://console.apify.com/``` para console.
