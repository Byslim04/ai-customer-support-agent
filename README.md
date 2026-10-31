# 🤖 AI Customer Support Agent

Автономный агент службы поддержки для интернет-магазина, построенный на базе RAG (Retrieval-Augmented Generation) и API-инструментов.

---

## 📌 Описание проекта

Проект предназначен для автоматизации обработки частых запросов клиентов интернет-магазина. Агент умеет:
* 📖 Искать ответы в базе знаний компании (RAG) по правилам доставки, возврата, оплаты, гарантии и контактам.
* 📦 Проверять актуальный статус заказа по его идентификатору (order_id) через эмулируемый API/CRM.
* 🔒 Работать в рамках строго определенных прав (только чтение данных, без изменения заказов или создания возвратов).
* 🛡️ Обрабатывать ошибки и защищать конфиденциальные данные клиентов.

---

## 🏗️ Архитектура и компоненты

Проект построен по следующей схеме взаимодействия:

1. Chat Trigger: Принимает входящие сообщения от пользователя.
2. AI Agent: Анализирует запрос и выбирает необходимый инструмент (RAG или API).
3. Tools (Инструменты):
   * **Search Knowledge Base**: Ищет информацию в документах компании из папки knowledge_base/.
   * **Get Order Status**: Запрашивает статус заказа через CRM/API.
4. Verified Context & Final Response: Сверяет полученные данные с правилами и формирует итоговый безопасный ответ пользователю.

---

## 📁 Структура базы знаний (knowledge_base/)

Документы компании разделены по категориям для корректной работы RAG:

* delivery_policy.txt — Сроки и условия доставки, информация о трек-номерах.
* return_policy.txt — Условия и правила возврата товаров надлежащего и ненадлежащего качества.
* payment_methods.txt — Доступные способы оплаты (онлайн, при получении).
* warranty_policy.txt — Условия гарантии и обмена бракованного товара.
* support_contacts.txt — Контакты и время работы службы поддержки.

---

## ⚙️ Использование инструментов (Tools)

### Tool 1: Search Knowledge Base
* Цель: Ответы на общие вопросы о правилах магазина.
* Примеры: «Каковы условия возврата?», «Сколько занимает доставка?».

### Tool 2: Get Order Status
* Цель: Запрос данных о конкретном заказе.
* Пример входящих данных: {"order_id": "A-1042"}
* Пример ответа API: 
  `json
  {
    "order_id": "A-1042",
    "status": "shipped",
    "tracking_number": "PL123456"
  }




----------




🤖 AI Customer Support Agent
An autonomous customer support agent for an online store, built using RAG (Retrieval-Augmented Generation) and API tools.

📌 Project Description
The project is designed to automate the handling of frequent customer inquiries for an online store. The agent is capable of:
- 📖 Searching for answers in the company's knowledge base (RAG) regarding delivery, returns, payment, warranty, and contact details.
- 📦 Checking the current order status by its identifier (order_id) via an emulated API/CRM.
- 🔒 Operating within strictly defined permissions (read-only access, no modifying orders or creating returns).
- 🛡️ Handling errors and protecting customer sensitive data.

🏗️ Architecture and Components
The project follows this interaction workflow:
1. Chat Trigger: Accepts incoming messages from the user.
2. AI Agent: Analyzes the query and selects the necessary tool (RAG or API).
3. Tools:
  - Search Knowledge Base: Searches for information in company documents from the `knowledge_base/` folder.
  - Get Order Status: Queries the order status via CRM/API.
4. Verified Context & Final Response: Cross-references the retrieved data with policies and generates a final safe response to the user.

📁 Knowledge Base Structure (`knowledge_base/`)
Company documents are categorized to ensure proper RAG performance:
- `delivery_policy.txt` — Delivery terms and conditions, tracking number information.
- `return_policy.txt` — Conditions and rules for returning eligible and defective items.
- `payment_methods.txt` — Available payment methods (online, cash on delivery).
- `warranty_policy.txt` — Warranty terms and exchange policy for defective goods.
- `support_contacts.txt` — Support service contacts and working hours.

⚙️ Using Tools
Tool 1: Search Knowledge Base
- Purpose: Answering general questions about store policies.
- Examples: "What are the return conditions?", "How long does delivery take?".

Tool 2: Get Order Status
- Purpose: Requesting details for a specific order.
- Input example: `{"order_id": "A-1042"}`
- API response example: 
  ```json
  {
    "order_id": "A-1042",
    "status": "shipped",
    "tracking_number": "PL123456"
  }
