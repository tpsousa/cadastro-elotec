

const user ="thiago";
const password  = 123;

const senhaSecreta = 1234;

//api -- autenticao,rotas,middlewares,tokens -- frameworks - django, - node , -spring boot

if (password == senhaSecreta){
    console.log("o usuario pode acessar a conta")
}else{
  console.log("ele nao pode acessar a conta");
}