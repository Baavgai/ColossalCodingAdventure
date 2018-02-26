var prompt = require('prompt');
prompt.start();

WELCOME = [
"Welcome to Camel Run!" ,
"You have stolen a camel (you egg!) to make your way across the great Mobi desert." ,
"The townspeople want their camel back and are chasing you down! Survive your" ,
"desert trek and outrun the blockos." ,
"Only drink when necessary. Always use E. to display your status!" ,
"Do not let your thirst go above 6 and your camel's tiredness above 8."
].join("\n")

Game.prototype.turn = function(){
  that = this;
  console.log('-----------------------')
  console.log(MENU)
  console.log('-----------------------')
  prompt.get( 'choice', function(error, result){
    that.parseResponse(result)
  });
};
