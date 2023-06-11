import csv
import json
import random
import time
import requests


def listing_page(link):
    url = link
    codes = []
    for page in [0, 1, 2]:
        payload = json.dumps({
            "operationName": "categories",
            "variables": {
                "query": ":bestseller:productitemtype:t-shirts:productitemtype:polos:productitemtype:henleys",
                "country": "US",
                "locale": "en_US",
                "currentPage": page,
                "pageSize": 36,
                "sort": "bestseller",
                "categoryId": "levi_clothing_men_shirts",
                "preOrder": False,
                "abTestSectionedPLP": False
            },
            "query": "query categories($query: String!, $sort: String, $currentPage: Int, $pageSize: Int, $categoryId: String!, $preOrder: Boolean, $abTestSectionedPLP: Boolean) {\n  categories(\n    query: $query\n    sort: $sort\n    currentPage: $currentPage\n    pageSize: $pageSize\n    categoryId: $categoryId\n    preOrder: $preOrder\n    abTestSectionedPLP: $abTestSectionedPLP\n  ) {\n    description\n    breadcrumbs {\n      facetCode\n      facetName\n      facetValueName\n      removeQuery {\n        query {\n          value\n        }\n        url\n      }\n    }\n    categoryCode\n    categoryHierarchy {\n      code\n      count\n      selected\n      childSelected\n      children\n      depth\n      leaf\n      parentSelected\n    }\n    categoryName\n    emailSignUpGateEnabled\n    registrationGateEnabled\n    currentQuery {\n      url\n    }\n    facets {\n      category\n      code\n      name\n      nofollow\n      priority\n      visible\n      topValues {\n        count\n        name\n        nofollow\n        selected\n        query {\n          query {\n            value\n          }\n          url\n        }\n      }\n      values {\n        count\n        name\n        nofollow\n        selected\n        query {\n          query {\n            value\n          }\n          url\n        }\n      }\n    }\n    freeTextSearch\n    noProductsRedirectMsg\n    lscoBreadcrumbs {\n      name\n      url\n      linkClass\n    }\n    pagination {\n      currentPage\n      totalPages\n      totalResults\n    }\n    products {\n      channels\n      code\n      backOrder\n      name\n      url\n      price {\n        code\n        currencyIso\n        formattedValue\n        hardPrice\n        hardPriceFormattedValue\n        regularPrice\n        regularPriceFormattedValue\n        softPrice\n        softPriceFormattedValue\n        value\n      }\n      priceRange {\n        maxPrice {\n          formattedValue\n          value\n          regularPrice\n          softPrice\n          hardPrice\n        }\n        minPrice {\n          formattedValue\n          value\n          regularPrice\n          softPrice\n          hardPrice\n        }\n      }\n      priceRangeFrom {\n        maxPrice {\n          formattedValue\n          value\n          regularPrice\n          softPrice\n          hardPrice\n        }\n        minPrice {\n          formattedValue\n          value\n          regularPrice\n          softPrice\n          hardPrice\n        }\n      }\n      baseProduct\n      soldIndividually\n      comingSoon\n      averageOverallRatings\n      noOfRatings\n      soldOutForever\n      sustainability\n      findInStoreEligible\n      customizable\n      flxCustomization\n      availableForPickup\n      department\n      pdpGroupId\n      preOrder\n      preOrderShipDate\n      returnable\n      variantOptions {\n        code\n        comingSoon\n        preOrder\n        backOrder\n        customizable\n        findInStoreEligible\n        flxCustomization\n        merchantBadge\n        promotionalBadge\n        sustainability\n        name\n        swatchUrl\n        swatchAltText\n        galleryList {\n          galleryImage {\n            altText\n            format\n            galleryIndex\n            imageType\n            url\n          }\n        }\n        priceData {\n          hardPrice\n          hardPriceFormattedValue\n          regularPrice\n          regularPriceFormattedValue\n          softPrice\n          softPriceFormattedValue\n          value\n          currencyIso\n        }\n        soldIndividually\n        soldOutForever\n        url\n      }\n      lscoBreadcrumbs {\n        categoryCode\n        name\n        url\n      }\n      swatchUrl\n      swatchAltText\n      galleryList {\n        galleryImage {\n          altText\n          format\n          galleryIndex\n          imageType\n          url\n        }\n      }\n      merchantBadge\n      promotionalBadge\n      errors {\n        component\n        name\n        time_thrown\n        message\n      }\n    }\n    seoMetaData {\n      canonicalUrl\n      metaDescription\n      metaH1\n      metaTitle\n      robots\n    }\n    sorts {\n      code\n      name\n      selected\n    }\n    spellingSuggestion {\n      query\n      suggestion\n    }\n    subSections {\n      description\n      categoryName\n      currentQuery {\n        url\n      }\n      pagination {\n        currentPage\n        totalPages\n        totalResults\n      }\n      products {\n        channels\n        code\n        backOrder\n        name\n        url\n        price {\n          code\n          currencyIso\n          formattedValue\n          hardPrice\n          hardPriceFormattedValue\n          regularPrice\n          regularPriceFormattedValue\n          softPrice\n          softPriceFormattedValue\n          value\n        }\n        priceRange {\n          maxPrice {\n            formattedValue\n            value\n            regularPrice\n            softPrice\n            hardPrice\n          }\n          minPrice {\n            formattedValue\n            value\n            regularPrice\n            softPrice\n            hardPrice\n          }\n        }\n        priceRangeFrom {\n          maxPrice {\n            formattedValue\n            value\n            regularPrice\n            softPrice\n            hardPrice\n          }\n          minPrice {\n            formattedValue\n            value\n            regularPrice\n            softPrice\n            hardPrice\n          }\n        }\n        baseProduct\n        soldIndividually\n        comingSoon\n        averageOverallRatings\n        noOfRatings\n        soldOutForever\n        sustainability\n        findInStoreEligible\n        customizable\n        flxCustomization\n        availableForPickup\n        department\n        pdpGroupId\n        preOrder\n        preOrderShipDate\n        returnable\n        variantOptions {\n          code\n          comingSoon\n          preOrder\n          backOrder\n          customizable\n          findInStoreEligible\n          flxCustomization\n          merchantBadge\n          promotionalBadge\n          sustainability\n          name\n          swatchUrl\n          swatchAltText\n          galleryList {\n            galleryImage {\n              altText\n              format\n              galleryIndex\n              imageType\n              url\n            }\n          }\n          priceData {\n            hardPrice\n            hardPriceFormattedValue\n            regularPrice\n            regularPriceFormattedValue\n            softPrice\n            softPriceFormattedValue\n            value\n            currencyIso\n          }\n          soldIndividually\n          soldOutForever\n          url\n        }\n        lscoBreadcrumbs {\n          categoryCode\n          name\n          url\n        }\n        swatchUrl\n        swatchAltText\n        galleryList {\n          galleryImage {\n            altText\n            format\n            galleryIndex\n            imageType\n            url\n          }\n        }\n        merchantBadge\n        promotionalBadge\n        errors {\n          component\n          name\n          time_thrown\n          message\n        }\n      }\n      seoMetaData {\n        canonicalUrl\n        metaDescription\n        metaH1\n        metaTitle\n        robots\n      }\n    }\n  }\n}\n"
        })

        headers = {
            'authority': 'www.levi.com',
            'accept': '*/*, application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'apollographql-client-name': 'WebApp',
            'apollographql-client-version': '0.1.0',
            'content-type': 'application/json',
            'cookie': 'ZIPCODE=Other; STATE=HR; LevisID=44457b72-b664-4195-a890-f8c231e2e0fc; at_check=true; AMCVS_B7FF1CFE5330995F0A490D45%40AdobeOrg=1; mboxEdgeCluster=31; crl8.fpcuid=e8d2ad3b-fbf0-458d-9ec4-c5198a5ac20e; TLTSID=85201382668353614853693539214867; _gcl_au=1.1.1159585028.1679913403; ConstructorioID_client_id=98e097b9-eca1-4f00-a1e9-455d94df1ce7; ajs_anonymous_id=84d21680-f975-4a24-a123-0ad84c28c6d2; lsa_fm=browse; s_cc=true; _ga=GA1.1.1100096751.1679913407; IR_gbd=levi.com; _fbp=fb.1.1679913407171.1220247471; ORA_FPC=id=f63761af-7a8a-464f-9d9b-bccd5e58ac9b; WTPERSIST=; QSI_SI_3eNzYi76yo7yYEB_intercept=true; BVBRANDID=1bd97d01-e605-4974-8ced-8b5092d4ab7d; _scid=50484453-1dbe-4e3a-b1d5-28e1648c117b; _tt_enable_cookie=1; _ttp=_J8GTYJSQn8jaE3Secd7r7Mfner; _pin_unauth=dWlkPVlqUmtaamt6TkRFdE56UTFNQzAwWmprMExXRmtZMll0T1RJellqVTFZakl6TkRCaA; _sctr=1|1679855400000; AMCV_B7FF1CFE5330995F0A490D45%40AdobeOrg=-330454231%7CMCIDTS%7C19444%7CMCMID%7C22956587252852478414494822514867800073%7CMCAAMLH-1680521797%7C12%7CMCAAMB-1680521797%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1679924197s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; alb_origin=Levi_EU_W_ng; ZIPCODE=Other; STATE=HR; AKA_A2=A; akaalb_levi1=1679923769~op=LB_Levi_Prod_WH_EU:Levi_Prod-WH_EU-1|prod_LB_Levi_EU_W:prod_Levi_EU_W_green_ng|~rv=44~m=Levi_Prod-WH_EU-1:0|prod_Levi_EU_W_green_ng:0|~os=05fae936b4a80c778b210cadb46bf07e~id=47a8cb724592205edfef751474ff9fb6; BVBRANDSID=8a1149f2-77cb-4f91-a2f3-505aaf70174c; s_sq=%5B%5BB%5D%5D; QSI_HistorySession=https%3A%2F%2Fwww.levi.com%2FUS%2Fen_US%2Fclothing%2Fmen%2Fshirts%2Fc%2Flevi_clothing_men_shirts%2Ffacets%2Fproductitemtype%2Ft-shirts%2Fproductitemtype%2Fpolos%2Fproductitemtype%2Fhenleys%2Fsort%2Fbestseller~1679922078329; mbox=PC#384a47580811472f918a9c0b80e93677.31_0#1743166952|session#ccb46c1c950d4f12aa6a502275003f17#1679923828; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+27+2023+18%3A32%3A31+GMT%2B0530+(India+Standard+Time)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=IN%3BHR; OptanonAlertBoxClosed=2023-03-27T13:02:31.885Z; IR_5398=1679922152949%7C0%7C1679922152949%7C%7C; IR_PI=469c9294-cc8b-11ed-8e07-551e40a9adf9%7C1680008552949; _uetsid=eff97b10cc8b11ed98f83bbae89094f5; _uetvid=eff9a590cc8b11eda66ffde49f602cfe; _ga_VV90TFYCDY=GS1.1.1679913406.1.1.1679922157.0.0.0; RT="z=1&dm=levi.com&si=7000db94-e071-4014-bd2a-74c99c288d2e&ss=lfqp1y2r&sl=1y&se=2s0&tt=38bf&bcn=%2F%2F684d0d41.akstat.io%2F"; STATE=HR; ZIPCODE=Other; alb_origin=Levi_EU_W_ng',
            'origin': 'https://www.levi.com',
            'referer': 'https://www.levi.com/US/en_US/clothing/men/shirts/c/levi_clothing_men_shirts/facets/productitemtype/t-shirts/productitemtype/polos/productitemtype/henleys/sort/bestseller',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'x-brand': 'levi',
            'x-country': 'US',
            'x-locale': 'en_US',
            'x-log-requesttime': '2023-03-27T13:02:37.621Z',
            'x-ngs-uniqueid': '44457b72-b664-4195-a890-f8c231e2e0fc--c413b496-b884-4692-b364-6e3376d2cff8',
            'x-operationname': 'categories',
            'x-selected-store': 'null',
            'x-sessionid': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJkZGRmZDc3My1iMjg0LTRhMDEtOWI2Ni05ZTcxYzM4MjNiM2IiLCJ1c2VySWQiOiJhbm9ueW1vdXMiLCJhY2Nlc3NUb2tlbiI6IiIsInJlZnJlc2hUb2tlbiI6IiIsImFjY2Vzc1Rva2VuRXhwaXJlcyI6IiIsImlzR3Vlc3QiOnRydWUsImxhc3RVcGRhdGVUaW1lIjoxNjc5OTIyMDc1MTkyLCJsb2dpbk9iaiI6eyJsb2dnZWRJbiI6ZmFsc2UsImxvZ2luRXhwaXJhdGlvbiI6bnVsbCwiaGFzRXhwaXJlZCI6ZmFsc2V9LCJpYXQiOjE2Nzk5MjIwNzUsImV4cCI6MTY3OTkyMzg3NSwiYXVkIjoiZ3JhcGhxbC51c2VyIiwiaXNzIjoibGV2aS53ZWJob29rcyIsInN1YiI6ImFwb2xsbyJ9.mI2nmciDuRwFzpU2Wu2y4EvsW5jCcA9WN12ZbOrNiN8sxYsmSc4p_AL6FYBkfzu-aI1tz1_wW94O-BzG6Dtddg'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        res = response.json()

        for row in res['data']['categories']['products']:
            link = row['url'].split('/')[-1]
            codes.append(link)
    print(codes)
    return codes


def product_data(code):
    url = "https://www.levi.com/nextgen-webhooks/?operationName=product&locale=US-en_US"

    payload = json.dumps({
        "operationName": "product",
        "variables": {
            "code": str(code)
        },
        "query": "query product($code: String!) {\n  product(code: $code) {\n    altText\n    averageOverallRatings\n    backOrder\n    baseProduct\n    bopisAvailable\n    channels\n    classifications {\n      code\n      features {\n        code\n        featureValues {\n          value\n          code\n        }\n        name\n        range\n        type\n      }\n      name\n    }\n    code\n    colorName\n    comingSoon\n    crossSellProductUrl\n    crossSellSizeGroup\n    customizable\n    flxCustomization\n    department\n    pdpGroupId\n    preOrder\n    preOrderShipDate\n    returnable\n    description\n    findInStoreEligible\n    lscoBreadcrumbs {\n      categoryCode\n      name\n      url\n    }\n    galleryImageList {\n      galleryImage {\n        altText\n        format\n        galleryIndex\n        imageType\n        url\n      }\n      videos {\n        altText\n        format\n        galleryIndex\n        url\n      }\n    }\n    itemType\n    maxOrderQuantity\n    merchantBadge\n    minOrderQuantity\n    name\n    noOfRatings\n    pdpCmsContentId1\n    pdpCmsContentId2\n    preferredCategory\n    price {\n      code\n      currencyIso\n      formattedValue\n      hardPrice\n      hardPriceFormattedValue\n      maxQuantity\n      minQuantity\n      priceType\n      regularPrice\n      regularPriceFormattedValue\n      softPrice\n      softPriceFormattedValue\n      value\n    }\n    productSchemaOrgMarkup {\n      brand {\n        entry {\n          key\n          value\n        }\n      }\n      gtin12\n      offers {\n        entry {\n          key\n          value\n        }\n      }\n    }\n    promotionalBadge\n    seoMetaData {\n      metaDescription\n      metaH1\n      metaTitle\n      robots\n    }\n    sizeGuide\n    soldIndividually\n    soldOutForever\n    url\n    variantLength\n    variantOptions {\n      code\n      colorName\n      displaySizeDescription\n      maxOrderQuantity\n      minOrderQuantity\n      priceData {\n        code\n        currencyIso\n        formattedValue\n        hardPrice\n        hardPriceFormattedValue\n        maxQuantity\n        minQuantity\n        priceType\n        regularPrice\n        regularPriceFormattedValue\n        softPrice\n        softPriceFormattedValue\n        value\n      }\n      stock {\n        asnDate\n        asnQty\n        stockLevel\n        stockLevelStatus\n      }\n      upc\n      url\n    }\n    variantSize\n    variantType\n    variantWaist\n    inventoryDepthStoresList\n  }\n}\n"
    })
    headers = {
        'authority': 'www.levi.com',
        'accept': '*/*, application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'apollographql-client-name': 'WebApp',
        'apollographql-client-version': '0.1.0',
        'content-type': 'application/json',
        'cookie': 'ZIPCODE=Other; STATE=HR; LevisID=44457b72-b664-4195-a890-f8c231e2e0fc; at_check=true; AMCVS_B7FF1CFE5330995F0A490D45%40AdobeOrg=1; mboxEdgeCluster=31; crl8.fpcuid=e8d2ad3b-fbf0-458d-9ec4-c5198a5ac20e; TLTSID=85201382668353614853693539214867; _gcl_au=1.1.1159585028.1679913403; ConstructorioID_client_id=98e097b9-eca1-4f00-a1e9-455d94df1ce7; ajs_anonymous_id=84d21680-f975-4a24-a123-0ad84c28c6d2; lsa_fm=browse; s_cc=true; _ga=GA1.1.1100096751.1679913407; IR_gbd=levi.com; _fbp=fb.1.1679913407171.1220247471; ORA_FPC=id=f63761af-7a8a-464f-9d9b-bccd5e58ac9b; WTPERSIST=; QSI_SI_3eNzYi76yo7yYEB_intercept=true; BVBRANDID=1bd97d01-e605-4974-8ced-8b5092d4ab7d; _scid=50484453-1dbe-4e3a-b1d5-28e1648c117b; _tt_enable_cookie=1; _ttp=_J8GTYJSQn8jaE3Secd7r7Mfner; _pin_unauth=dWlkPVlqUmtaamt6TkRFdE56UTFNQzAwWmprMExXRmtZMll0T1RJellqVTFZakl6TkRCaA; _sctr=1|1679855400000; AMCV_B7FF1CFE5330995F0A490D45%40AdobeOrg=-330454231%7CMCIDTS%7C19444%7CMCMID%7C22956587252852478414494822514867800073%7CMCAAMLH-1680521797%7C12%7CMCAAMB-1680521797%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1679924197s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; alb_origin=Levi_EU_W_ng; ZIPCODE=Other; STATE=HR; AKA_A2=A; akaalb_levi1=1679923769~op=LB_Levi_Prod_WH_EU:Levi_Prod-WH_EU-1|prod_LB_Levi_EU_W:prod_Levi_EU_W_green_ng|~rv=44~m=Levi_Prod-WH_EU-1:0|prod_Levi_EU_W_green_ng:0|~os=05fae936b4a80c778b210cadb46bf07e~id=47a8cb724592205edfef751474ff9fb6; BVBRANDSID=8a1149f2-77cb-4f91-a2f3-505aaf70174c; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+27+2023+18%3A51%3A12+GMT%2B0530+(India+Standard+Time)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=IN%3BHR; OptanonAlertBoxClosed=2023-03-27T13:21:12.845Z; IR_5398=1679923273077%7C0%7C1679923273077%7C%7C; IR_PI=469c9294-cc8b-11ed-8e07-551e40a9adf9%7C1680009673077; s_sq=%5B%5BB%5D%5D; QSI_HistorySession=https%3A%2F%2Fwww.levi.com%2FUS%2Fen_US%2Fclothing%2Fmen%2Fshirts%2Fc%2Flevi_clothing_men_shirts%2Ffacets%2Fproductitemtype%2Ft-shirts%2Fproductitemtype%2Fpolos%2Fproductitemtype%2Fhenleys%2Fsort%2Fbestseller%3Fpage%3D1~1679923358625%7Chttps%3A%2F%2Fwww.levi.com%2FUS%2Fen_US%2Fsale%2Fmens-sale%2Fshirts%2Fthe-essential-t-shirt%2Fp%2FA33280005~1679923361931; mbox=PC#384a47580811472f918a9c0b80e93677.31_0#1743168164|session#ccb46c1c950d4f12aa6a502275003f17#1679923828; _uetsid=eff97b10cc8b11ed98f83bbae89094f5; _uetvid=eff9a590cc8b11eda66ffde49f602cfe; _ga_VV90TFYCDY=GS1.1.1679913406.1.1.1679923379.0.0.0; RT="z=1&dm=levi.com&si=7000db94-e071-4014-bd2a-74c99c288d2e&ss=lfqp1y2r&sl=23&se=2s0&tt=3k47&bcn=%2F%2F684d0d41.akstat.io%2F"; STATE=HR; ZIPCODE=Other; alb_origin=Levi_EU_W_ng',
        'origin': 'https://www.levi.com',
        'referer': 'https://www.levi.com/US/en_US/sale/mens-sale/shirts/the-essential-t-shirt/p/A33280005',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-brand': 'levi',
        'x-country': 'US',
        'x-locale': 'en_US',
        'x-log-requesttime': '2023-03-27T13:22:59.818Z',
        'x-ngs-uniqueid': '44457b72-b664-4195-a890-f8c231e2e0fc--d1fe9aa2-2ed1-44fd-944a-294d03ec2f11',
        'x-operationname': 'product',
        'x-selected-store': 'null',
        'x-sessionid': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJkZGRmZDc3My1iMjg0LTRhMDEtOWI2Ni05ZTcxYzM4MjNiM2IiLCJ1c2VySWQiOiJhbm9ueW1vdXMiLCJhY2Nlc3NUb2tlbiI6IiIsInJlZnJlc2hUb2tlbiI6IiIsImFjY2Vzc1Rva2VuRXhwaXJlcyI6IiIsImlzR3Vlc3QiOnRydWUsImxhc3RVcGRhdGVUaW1lIjoxNjc5OTIyODIyNzM4LCJsb2dpbk9iaiI6eyJsb2dnZWRJbiI6ZmFsc2UsImxvZ2luRXhwaXJhdGlvbiI6bnVsbCwiaGFzRXhwaXJlZCI6ZmFsc2V9LCJpYXQiOjE2Nzk5MjI4MjIsImV4cCI6MTY3OTkyNDYyMiwiYXVkIjoiZ3JhcGhxbC51c2VyIiwiaXNzIjoibGV2aS53ZWJob29rcyIsInN1YiI6ImFwb2xsbyJ9.nBHe6UxDBpncXSW7mHe6svCYEnMmFTMWtWHkuPjRuKzGiM04wDnPAV2yG6NtgjDzqPaupxXzMJZSj-LXu7BbbQ'
    }

    resp = requests.request("POST", url, headers=headers, data=payload)
    r = resp.json()
    # print(r)
    product_link = "https://www.levi.com/US/en_US"+r['data']['product']['url']
    name = r['data']['product']['name']
    rating = r['data']['product']['averageOverallRatings']
    color = r['data']['product']['colorName']
    image = r['data']['product']['galleryImageList']['galleryImage'][0]['url']
    size = r['data']['product']['variantSize']
    description = r['data']['product']['description']
    price = r['data']['product']['price']['formattedValue']
    features = r['data']['product']['classifications']

    data = {
        'product_link': product_link,
        'product name': name,
        'color': color,
        'image': image,
        'price': price,
        'ratings': rating,
        'Available sizes': size,
        'features': features,
        'description': description
    }
    print(data)
    return data


def main():
    url = "https://www.levi.com/nextgen-webhooks/?operationName=categories&locale=US-en_US"
    product_codes = listing_page(url)
    print(f"Total URLs : {len(product_codes)}")
    filename = 'us-levis-men-t-shirts.csv'
    fieldnames = ['product_link', 'product name', 'color', 'image', 'price', 'ratings', 'Available sizes', 'description', 'features']
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for code in product_codes:
            data = product_data(code)
            time.sleep(random.randint(1, 10))
            writer.writerow(data)


if __name__ == '__main__':
    main()