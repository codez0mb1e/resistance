# Антикризисный риск-менеджмент личных финансов

![Status](https://img.shields.io/badge/status-in_active_development-green.svg)
[![Contributors Welcome](https://img.shields.io/badge/contributing-welcome-blue.svg)](CONTRIBUTING.md)
[![GitHub license](https://img.shields.io/badge/license-CC0-blue.svg)](LICENSE)

***Риск-менеджмент личных финансов условиях санкций и/или финансового кризиса: делаем сегодня все, чтобы завтра избежать фатальных последствий.***

:white_check_mark: В рамках проекта рассматривается использование *исключительно экономических* методов (поскольку они снижают риски для индивидуума) по минимизации финансовых рисков.

:x: В рамках проекта не рассматривает использование никаких *политических* приемов (они важны, но увеличивают риски для индивидуума).

---

- :warning: Непонимание работы используемых инвестиционных инструментов: акций, облигаций, криптовалюты и/или производных финансовых инструментов - несет в себе **риски полной утраты средств**.
- :warning: Несоблюдение правил ИТ-безопасности, таких как сильные неповторяющиеся пароли, 2FA, [безопасный браузер](lists.md#список-софта), [защищенное соединение](lists.md#vpn) - несет в себе **риски полной утраты средств**.
- :warning: Невыполнение [законодательства](lists.md#законодательные-акты) юрисдикций, через которые происходит инвестирование, несет в себе **риски полной утраты средств**.
- :warning: Слепое следование чужим инвестиционным идеям несет в себе **риски полной утраты средств**.

*Ничего из перечисленного в данном репозитории не является финансовой рекомендацией.*

---

:newspaper: **Последние обновления**:

Июнь 2022:

- Обновлены [требования к брокерам](lists.md#требования-к-брокерам)
- Обновлена информация [по блокировкам со стороны Coinbase](lists.md#криптобиржи)
- Обновлена информация [VPN сервисам](lists.md#vpn-cервисы).

Maй 2022:

- Отразил кейс с обвалом стейблкоина UST на ~~>70%~~ 100% в [сравнительной таблице стейблкоинов](lists.md#stablecoins)

Апрель 2022:

- Binance: [aктуализация органичений для резидентов РФ](sanctions-risks-in-cryptocurrency.md#pushpin-где-хранить-а-что-не-стоит).
- Расширенное сравнение для:
  - [стейблкоинов](lists.md#stablecoins)
  - [VPN сервисов](lists.md#vpn)
  - [кошельков](lists.md#некастодиальные-кошельки).
- Для формирования низкорискованного валютного портфеля:
  - добавил скрипт [анализа волатильности валют](src/fx_currencies_analysis.md)
  - добавил скрипт [моделирования цен валют с использованием метода Монте-Карло](src/fx_currency_portfolio__assets_selection.ipynb).

Март 2022:

- Обновление списка [стейблкоинов](lists.md#stablecoins)
- Рефакторинг списка [VPN сервисов](lists.md#vpn)
- Обновлена структура `README.md`
- Уточнен список бирж, вводивших ограничения против резидентов РФ
- Добавлена секция [Важные новости](sanctions-risks-in-cryptocurrency.md#важные-новости) в части санкций, касаюющих криптобирж.

---

## Введение в риски: сценарии развития

- [Глупые стратегии и большие риски](introduction-to-risks.md#глупые-стратегии-и-большие-риски)
- [Сценарий I: «Черный день»](introduction-to-risks.md#сценарий-i-черный-день)
  - [Цель](introduction-to-risks.md#цель)
  - [План](introduction-to-risks.md#план)
  - [Сроки](introduction-to-risks.md#сроки)
- [Сценарий II: Блэкаут](introduction-to-risks.md#сценарий-ii-блэкаут)
  - [Цель](introduction-to-risks.md#цель-1)
  - [План](introduction-to-risks.md#план-1)
  - [Сроки](introduction-to-risks.md#сроки-1)
- [Сценарий III: Утрата сбережений](introduction-to-risks.md#сценарий-iii-утрата-сбережений)
  - [Цель](introduction-to-risks.md#цель-2)
  - [План](introduction-to-risks.md#план-2)
  - [Сроки](introduction-to-risks.md#сроки-2)
- [Итак...](introduction-to-risks.md#итак)
- [~~Общее~~ Важное](introduction-to-risks.md#общее-важное)

Итоговая таблица: 

| Где хранится | Соотношение RUB/USD | Риски обесценивания на горизонте года | Риски утраты контроля | Вывод средств потенциально может быть невозможен в течение... |
| -- | -- | -- | -- | -- |
| Наличные средства | 70% RUB, 30% USD | Очень высокие | Низкие | Средства могут быть изъяты в любой момент |
| Инвест-счета у российских брокеров | 50% RUB, 50% USD/EUR | Высокие | Средние | 0.5-1 год |
| Инвест-счета у иностранных брокеров | 100% USD | Низкие | Высокие | 1-3 года |
| Инвест-счета у крипто брокеров | 100% USD | Средние | Средние | 1-3 года |
| Холодный крипто кошелек | 100% USD | Средние | Низкие | 1-3 года |

*[Пост и обсуждения](https://habr.com/ru/post/654313/) на Habr.*

## Инвестиции в криптовалюту: риск-менеджмент в условии санкций

- [TL;DR](sanctions-risks-in-cryptocurrency.md#tldr)
- [0. Правила игры (подготовка)](sanctions-risks-in-cryptocurrency.md#0-правила-игры-подготовка)
- [1. Что хранить?](sanctions-risks-in-cryptocurrency.md#1-что-хранить)
  - [Криптовалюта со свободным курсом](sanctions-risks-in-cryptocurrency.md#криптовалюта-со-свободным-курсом)
  - [Стейблкоин](sanctions-risks-in-cryptocurrency.md#стейблкоин)
  - [:pushpin: Что хранить... а что не стоит](sanctions-risks-in-cryptocurrency.md#pushpin-что-хранить-а-что-не-стоит)
- [2. Где хранить?](sanctions-risks-in-cryptocurrency.md#2-где-хранить)
  - [Биржи](sanctions-risks-in-cryptocurrency.md#биржи)
  - [Кошельки](sanctions-risks-in-cryptocurrency.md#кошельки)
  - [:pushpin: Где хранить... а где не стоит](sanctions-risks-in-cryptocurrency.md#pushpin-где-хранить-а-где-не-стоит)
- [Итак](sanctions-risks-in-cryptocurrency.md#итак)
- [:date: Важные новости](sanctions-risks-in-cryptocurrency.md#date-важные-новости)
- [Полезные ссылки](sanctions-risks-in-cryptocurrency.md#полезные-ссылки)

Итоговая таблица: 

| Где? | Что? | Цель | Горизонт | Аналог на классических финансовых рынков | Риски просадки стоимости | Риски hack'ов | Риски блокировки средств (текущие) | Риски блокировки в случае санкций |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| **CEX** биржа (кастодиальный кошелек) | Криптовалюты с плавающей стоимостью | Краткосрочные и высокорискованные инвестиции | Внутридневная торговля | Спекулятивная торговля на бирже | Самые высокие | Низкие | Умеренные | Самые высокие |
| **DEX** биржа (некастодиальный кошелек) | Криптовалюты с плавающей стоимостью | Среднесрочные инвестиции | 1-3 года | Инвестиции в акции | Высокие | Умеренные | Низкие | Умеренные |
| **Приложение-кошелек** (некастодиальный кошелек) | Криптовалютные портфели с плавающей стоимостью | Средне- или долгосрочные инвестиции | ~3 года | Инвестиции в акции и ETF | Умеренные* | Низкие | Низкие | Низкие |
| **DEX** биржа (некастодиальный кошелек) | Стейкинг пар с криптовалютой | Сбережения в валюте с защитой от инфляции | - | **Валютный депозит в банке** | Низкие | Умеренные | Низкие | Умеренные |
| **Приложение-кошелек** (некастодиальный кошелек) | Алгоритмические стейблкоины | Хэджирование валютных рисков | - | **Счет в долларах в банке** | Низкие | Низкие | Низкие | Низкие |
| **Холодный кошелек** (некастодиальный) | BTC и ETH (не более 10%), алгоритмические стейблкоины | Надежно спрятать сбережения | от 3 лет | Банковская ячейка с долларами, золотом, акциями FAANG | Низкие** | Самые низкие | Самые низкие | Самые низкие |

\* На горизонте 3 лет с ребалансировкой портфеля.

\** Инфляция "ест" сбержения.

*[Пост и обсуждения](https://habr.com/ru/post/655735/) на Habr.*

## Инфраструктура: важные списки

- [Законодательные акты](lists.md#законодательные-акты)
  - [Ограничения по операция с иностранной валюты](lists.md#ограничения-по-операция-с-иностранной-валюты)
  - [Список недружественных государств](lists.md#список-недружественных-государств)
  - [Полезные ссылки](lists.md#полезные-ссылки)
- [Список надежных российских банков](lists.md#список-надежных-российских-банков)
  - [Требования к банкам](lists.md#требования-к-банкам)
  - [Банки под санкциями](lists.md#банки-под-санкциями)
  - [Список надежных банков](lists.md#список-надежных-банков)
  - [Полезные ссылки](lists.md#полезные-ссылки-1)
- [Список надежных российских брокеров](lists.md#список-надежных-российских-брокеров)
  - [Иностранные брокеры](lists.md#иностранные-брокеры)
  - [Российские брокеры](lists.md#российские-брокеры)
  - [Полезные ссылки](lists.md#полезные-ссылки-2)
- [Надежные почтовые сервисы](lists.md#надежные-почтовые-сервисы)
  - [Российские почтовые сервисы](lists.md#российские-почтовые-сервисы)
  - [Иностранные почтовые сервисы](lists.md#иностранные-почтовые-сервисы)
- [Криптовалюты](lists.md#криптовалюты)
  - [Stablecoins](lists.md#stablecoins)
  - [Некастодиальные кошельки](lists.md#некастодиальные-кошельки)
  - [Криптобиржи](lists.md#криптобиржи)
  - [Сервисы поиска обменников](lists.md#сервисы-поиска-обменников)
- [VPN](lists.md#vpn)
  - [VPN cервисы](lists.md#vpn-cервисы)
  - [Другие инструменты обхода блокировок](lists.md#другие-инструменты-обхода-блокировок)
  - [Полезные ссылки](lists.md#полезные-ссылки-3)
- [Список софта](lists.md#список-софта)


## FAQ

**Для наличных средств**:

- [В какой валюте хранить наличные средства?](faq.md#в-какой-валюте-хранить-наличные-средства)
- [Как выбрать соотношение рублей, иностранной валюты для наличных средств?](faq.md#как-выбрать-соотношение-рублей-иностранной-валюты-для-наличных-средств)
