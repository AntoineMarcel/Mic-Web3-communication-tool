$(document).ready(function () {
      var receiver = null
      var signer = null

      $("#micCloseModal").click(function () {
            $("#micModal").hide()
      });

      $("#micConnect").click(function () {
            micConnectWallet();
      });

      async function micConnectWallet() {
            if (window.ethereum != null) {
                  try {
                        await window.ethereum.request({ method: 'eth_requestAccounts' });
                        const provider = new ethers.providers.Web3Provider(window.ethereum);

                        signer = provider.getSigner();
                        receiver = await signer.getAddress();
                        const verify = await fetch(`https://app.joinmic.xyz/status/${sender}/${receiver}`, { method: "GET" })
                        const status = ((await verify.json())["status"])
                        if (status == "not authorized") {
                              authorize()
                        }
                        else if (status == "error") {
                              $("#micModal").show()
                        }
                        else {
                              micAfterConnected(false)
                        }
                  } catch (error) {
                        console.log(error)
                        return false;
                  }
            }
            else
            {
                  $("#micConnect").text("Please install Metamask")
            }
      }

      $("#micModalForm").submit(function (event) {
            authorize($("#micEmailModal").val());
            $("#micModal").hide()
            event.preventDefault();
      });

      async function authorize(email) {
            const sig = await signer.signMessage(`Authorize ${sender} to send mails`)
            const manage = email == null ?
                  await fetch(`https://app.joinmic.xyz/manage/${sender}/${receiver}/${sig}`, { method: "GET" })
                  :
                  await fetch(`https://app.joinmic.xyz/manage/${sender}/${receiver}/${sig}/${email}`, { method: "GET" })
            const status = ((await manage.json())["status"])
            if (status == "success") {
                  micAfterConnected(true)
            }
      }
});