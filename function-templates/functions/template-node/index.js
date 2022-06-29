async function cloudFunction(params) {
  const body = params;
  const input1 = body['input1']
  const response = {
    input1: input1
  };

  return response;
}

//AWS CALL
exports.handler = async (event) => {  
  const body = JSON.parse(event.body);
  result = await cloudFunction(body)
  return {
    statusCode: 200,
    body: JSON.stringify({
      input1: result.input1,
    }),
  };
};

//IBM
exports.main = cloudFunction;