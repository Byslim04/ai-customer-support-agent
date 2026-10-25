import os
import json

# ==========================================
# Tool 1: Search Knowledge Base (RAG Search)
# ==========================================
def search_knowledge_base(query: str, kb_folder: str = "knowledge_base") -> str:
    """Простой поиск по текстовым файлам базы знаний (эмуляция RAG)."""
    results = []
    if not os.path.exists(kb_folder):
        return "База знаний недоступна."

    query_words = query.lower().split()
    
    for file_name in os.listdir(kb_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(kb_folder, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if any(word in content.lower() for word in query_words):
                    results.append(f"--- Из файла {file_name} ---\n{content.strip()}")
                    
    if results:
        return "\n\n".join(results)
    return "К сожалению, в базе знаний нет информации по вашему запросу."


# ==========================================
# Tool 2: Get Order Status (API/CRM)
# ==========================================
MOCK_ORDERS_DB = {
    "A-1042": {"order_id": "A-1042", "status": "shipped", "tracking_number": "PL123456"},
    "B-2050": {"order_id": "B-2050", "status": "processing", "tracking_number": None},
    "C-3099": {"order_id": "C-3099", "status": "delivered", "tracking_number": "PL987654"}
}

def get_order_status(order_id: str) -> str:
    """Получает статус заказа из CRM по его ID."""
    order = MOCK_ORDERS_DB.get(order_id.upper())
    if order:
        return json.dumps(order, ensure_ascii=False, indent=2)
    return json.dumps({"error": f"Заказ {order_id} не найден."}, ensure_ascii=False)


# ==========================================
# AI Support Agent Core (Логика агента)
# ==========================================
def run_support_agent(user_message: str):
    print(f"\n👤 Сообщение пользователя: '{user_message}'")
    
    words = user_message.lower().split()
    order_id = None
    for word in words:
        clean_word = word.strip("?,.!")
        if clean_word.upper().startswith("A-") or clean_word.upper().startswith("B-") or clean_word.upper().startswith("C-"):
            order_id = clean_word.upper()
            break
            
    if order_id:
        print(f"🤖 [Agent]: Обнаружен запрос статуса заказа. Вызов Tool 2 (Get Order Status)...")
        status_json = get_order_status(order_id)
        data = json.loads(status_json)
        
        if "error" in data:
            print(f"🤖 [Agent]: {data['error']}")
        else:
            print(f"🤖 [Agent]: Заказ {data['order_id']} имеет статус '{data['status']}'. Трек-номер: {data['tracking_number'] or 'еще не назначен'}.")
        return

    print(f"🤖 [Agent]: Вызов Tool 1 (Search Knowledge Base)...")
    kb_result = search_knowledge_base(user_message)
    print(f"🤖 [Agent]: Ответ из базы знаний:\n{kb_result}")


if name == "main":
    print("=== Запуск AI Customer Support Agent ===")
    run_support_agent("Сколько занимает доставка?")
    run_support_agent("Где мой заказ A-1042?")
    run_support_agent("Как вернуть товар?")
