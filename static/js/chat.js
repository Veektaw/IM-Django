let chatSocket;
let username;
let roomName;

document.addEventListener('DOMContentLoaded', function () {
  roomName = JSON.parse(document.getElementById('json-roomname').textContent);
  username = JSON.parse(document.getElementById('json-username').textContent); // Corrected variable name
  chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/');

  chatSocket.onopen = function (e) {
    // Once the WebSocket connection is open, enable the form submission button
    document.querySelector('#chat-message-submit').disabled = false;
  };

  chatSocket.onmessage = function (e) {
    console.log(e.data);
    const message = JSON.parse(e.data);

    if (message.message) {
      const createdAt = new Date(message.created_at).toLocaleString();
      let html = '';
      if (message.username === username) {
        // Right column for the sender's messages
        html += '<div class="msg right-msg">';
        // html += '<div class="msg-img" style="background-image: url(https://image.flaticon.com/icons/svg/145/145867.svg)"></div>'; // Add the message sender's avatar
      } else {
        // Left column for the receiver's messages
        html += '<div class="msg left-msg">';
        // html += '<div class="msg-img" style="background-image: url(https://image.flaticon.com/icons/svg/327/327779.svg)"></div>'; // Add the default avatar for the receiver
      }

      html += '<div class="msg-bubble">';
      html += '<div class="msg-info">';
      html += '<div class="msg-info-name">' + message.username + '</div>';
      html += '<div class="msg-info-time">' + createdAt + '</div>';
      html += '</div>';
      html += '<div class="msg-text">' + message.message + '</div>';
      html += '</div>';
      html += '</div>';

      // Append the new chat bubble to the container
      const chatMessagesContainer = document.querySelector('#chat-messages-container');
      chatMessagesContainer.innerHTML += html;

      // Scroll to the bottom of the chat container
      chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
    } else {
      alert('The message was empty');
    }
  };
});

document.querySelector('#chat-message-submit').onclick = function (e) {
  e.preventDefault(); // Prevent default form submission
  const messageInputDom = document.querySelector('#chat-message-input');
  const message = messageInputDom.value;

  chatSocket.send(JSON.stringify({
    'message': message,
    'username': username, // Corrected variable name
    'room': roomName, // Make sure 'room' is included in the data sent to the backend
  }));

  messageInputDom.value = '';
  return false;
};
