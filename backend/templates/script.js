var sender = "support@buildspace.app"
var receiver = null
var signer = null
var isConnected = false

$("#closeModal").click(function () {
      $("#myModal").hide()
});

$("#demo").click(function () {
      test();
});

async function test() {
      if (window.ethereum != null) {
            try {
                  await window.ethereum.request({ method: 'eth_requestAccounts' });
                  const provider = new ethers.providers.Web3Provider(window.ethereum);

                  signer = provider.getSigner();
                  receiver = await signer.getAddress();
                  const verify = await fetch(`https://amarcel.pythonanywhere.com/status/${sender}/${receiver}`, { method: "GET" })
                  const status = ((await verify.json())["status"])
                  if (status == "not authorized") {
                        authorize()
                  }
                  else if (status == "error") {
                        $("#myModal").show()
                  }
                  else {
                        isConnected = true
                        isConnected()
                  }
            } catch (error) {
                  console.log(error)
                  return false;
            }
      }
}

$("#modalForm").submit(function (event) {
      authorize($("#emailModal").val());
      $("#myModal").hide()
      event.preventDefault();
});

async function authorize(email) {
      const sig = await signer.signMessage("Authorize support@buildspace.app to send mails")
      const manage = email == null ?
            await fetch(`https://amarcel.pythonanywhere.com/manage/${sender}/${receiver}/${sig}`, { method: "GET" })
            :
            await fetch(`https://amarcel.pythonanywhere.com/manage/${sender}/${receiver}/${sig}/${email}`, { method: "GET" })
      const status = ((await manage.json())["status"])
      if (status == "success") {
            isAuthorized = true
            isConnected()
      }
}