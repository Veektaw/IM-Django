// chat.js

$(document).ready(function () {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/' + document.querySelector('body').getAttribute('data-user') + '/'
    );
  
    chatSocket.onopen = function () {
      console.log('WebSocket connection established.');
    };
  
    chatSocket.onmessage = function (event) {
      // Handle incoming messages from the WebSocket server
      const data = JSON.parse(event.data);
      const message = data.message;
      const sender = data.username;
  
      // Display the received message in the chat window
      const chatBox = $('.msger-chat');
      const messageHtml = `<div class="msg left-msg">
          <div class="msg-bubble">
              <div class="msg-info">
                  <div class="msg-info-name">${sender}</div>
                  <div class="msg-info-time">${getCurrentTime()}</div>
              </div>
              <div class="msg-text">${message}</div>
          </div>
      </div>`;
      chatBox.append(messageHtml);
    };
  
    chatSocket.onclose = function (event) {
      console.error('WebSocket closed unexpectedly.', event);
    };
  
    // Handle form submission to send messages
    $('.msger-inputarea').on('submit', function (event) {
      event.preventDefault();
      const messageInput = $('.msger-input');
      const message = messageInput.val().trim();
      if (message !== '') {
        // Send the message to the server using AJAX
        $.ajax({
          type: 'POST',
          url: '/send_message/', // Replace with your view URL to handle message sending
          data: {
            message: message,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function (response) {
            messageInput.val('');
          },
          error: function (error) {
            console.error('Error sending message:', error);
          },
        });
      }
    });
  });
  
  function getCurrentTime() {
    // Return the current time in the format HH:mm
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    return `${hours}:${minutes}`;
  }
  