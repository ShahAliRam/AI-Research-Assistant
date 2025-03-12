document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    
    // Auto-resize textarea as user types
    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
    
    // Handle form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addMessage(message, 'human');
        
        // Clear input and reset height
        userInput.value = '';
        userInput.style.height = 'auto';
        
        // Scroll to bottom
        scrollToBottom();
        
        // Send message to server and get response
        sendMessage(message);
    });
    
    function addMessage(text, sender, time = getCurrentTime()) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        
        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${formatMessage(text)}</p>
            </div>
            <div class="message-time">${time}</div>
        `;
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }
    
    function formatMessage(text) {
        // Convert URLs to links
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        text = text.replace(urlRegex, '<a href="$1" target="_blank">$1</a>');
        
        // Convert line breaks to <br>
        return text.replace(/\n/g, '<br>');
    }
    
    function sendMessage(message) {
        // Show typing indicator
        showTypingIndicator();
        
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add assistant response
            addMessage(data.response, 'assistant', data.timestamp);
        })
        .catch(error => {
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add error message
            addMessage('Sorry, there was an error processing your request. Please try again.', 'assistant');
            console.error('Error:', error);
        });
    }
    
    function showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.classList.add('message', 'assistant', 'typing-indicator');
        
        indicator.innerHTML = `
            <div class="message-content">
                <p>Thinking<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></p>
            </div>
        `;
        
        chatMessages.appendChild(indicator);
        scrollToBottom();
    }
    
    function removeTypingIndicator() {
        const indicator = document.querySelector('.typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }
    
    function getCurrentTime() {
        const now = new Date();
        return now.getHours().toString().padStart(2, '0') + ':' + 
               now.getMinutes().toString().padStart(2, '0');
    }
    
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Add event listener for Enter key (submit) and Shift+Enter (new line)
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    });
});