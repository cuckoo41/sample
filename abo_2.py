    #################################################
    # IxLoad ScriptGen created script
    # Test1 serialized using version 8.50.115.124
    # abo_2.py made on 4 19 2019 09:59
    #################################################
    


from IxLoad import IxLoad

IxLoad = IxLoad()

IxLoad.connect("1.2.3.4")


try:

    logtag = "IxLoad-api"
    logName = "abo_2"
    logger = IxLoad.new("ixLogger", logtag, 1)
    logEngine = logger.getEngine()
    logEngine.setLevels(IxLoad.ixLogger.kLevelDebug, IxLoad.ixLogger.kLevelInfo)
    logEngine.setFile(logName, 5, 256, 1)

    IxLoad.loadAppPlugin("HTTP")

    #################################################
    # Build chassis chain
    #################################################
    chassisChain = IxLoad.new("ixChassisChain")

    chassisChain.addChassis("192.168.1.210")

    Test1 = IxLoad.new("ixTest")

    scenarioElementFactory = Test1.getScenarioElementFactory()

    scenarioFactory = Test1.getScenarioFactory()

    #################################################
    # Profile Directory
    #################################################
    profileDirectory = Test1.cget("profileDirectory")

    my_ixEventHandlerSettings = IxLoad.new("ixEventHandlerSettings")

    my_ixEventHandlerSettings.config(
        disabledEventClasses = "",
        disabledPorts = ""
)

    my_ixViewOptions = IxLoad.new("ixViewOptions")

    my_ixViewOptions.config(
        runMode = 1,
        captureRunDuration = 0,
        captureRunAfter = 0,
        collectScheme = 0,
        allocatedBufferMemoryPercentage = 30
)

    Test1.scenarioList.clear()

    Scenario1 = scenarioFactory.create("Scenario")

    Scenario1.columnList.clear()

    Originate = IxLoad.new("ixTrafficColumn")

    Originate.elementList.clear()

    #################################################
    # Create ScenarioElement kSubscriberNetTraffic
    #################################################
    Subscriber2_Network1 = scenarioElementFactory.create(IxLoad.ixScenarioElementType.kSubscriberNetTraffic)

    

    my_ixPortL1Settings = IxLoad.new("ixPortL1Settings")

    my_ixPortL1Settings.config(
        useIEEEDefaults = True,
        requestRSFEC = False,
        autoNegotiate = False,
        enableRSFECStatistics = False,
        fecValue = 3,
        advertiseRSFEC = False,
        requestFCFEC = False,
        enableRSFEC = False,
        advertiseFCFEC = False
)

    #################################################
    # Network Network1 of NetTraffic Subscriber2@Network1
    #################################################
    Network1 = Subscriber2_Network1.cget("network")

    Network1.portList.appendItem(
        chassisId = 1,
        cardId = 1,
        portId = 1
)

    Network1.portList[0].setPortCaptureEnable(True)

    Network1.portList[0].setPortCaptureFileName("RESULTS\\\\abo_2\\\\Port_1_1_1_capture.cap")

    Network1.globalPlugins.clear()

    

    Settings_3 = IxLoad.new("ixNetIxLoadSettingsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = Settings_3
)

    

    Settings_3.config(
        teardownInterfaceWithUser = False,
        _Stale = False,
        itemType = "IxLoadSettingsPlugin",
        interfaceBehavior = 1
)

    Filter_4 = IxLoad.new("ixNetFilterPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = Filter_4
)

    

    Filter_4.config(
        all = False,
        pppoecontrol = False,
        isis = False,
        itemType = "FilterPlugin",
        auto = True,
        udp = "",
        tcp = "",
        mac = "",
        _Stale = False,
        pppoenetwork = False,
        ip = "",
        icmp = ""
)

    GratARP_4 = IxLoad.new("ixNetGratArpPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = GratARP_4
)

    

    GratARP_4.config(
        itemType = "GratArpPlugin",
        forwardGratArp = False,
        enabled = True,
        maxFramesPerSecond = 0,
        _Stale = False,
        rateControlEnabled = False
)

    TCP_3 = IxLoad.new("ixNetTCPPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = TCP_3
)

    

    TCP_3.config(
        tcp_bic = 0,
        tcp_tw_recycle = True,
        tcp_retries2 = 5,
        itemType = "TCPPlugin",
        disable_min_max_buffer_size = True,
        tcp_retries1 = 3,
        tcp_keepalive_time = 7200,
        tcp_mgmt_rmem = 87380,
        tcp_rfc1337 = False,
        tcp_ipfrag_time = 30,
        tcp_rto_max = 120000,
        tcp_window_scaling = False,
        delayed_acks = True,
        udp_port_randomization = False,
        tcp_vegas_alpha = 2,
        tcp_vegas_beta = 6,
        tcp_wmem_max = 262144,
        tcp_ecn = False,
        tcp_westwood = 0,
        tcp_rto_min = 200,
        delayed_acks_segments = 0,
        tcp_vegas_cong_avoid = 0,
        tcp_keepalive_intvl = 75,
        tcp_rmem_max = 262144,
        tcp_orphan_retries = 0,
        bestPerfSettings = False,
        tcp_max_tw_buckets = 180000,
        _Stale = False,
        tcp_low_latency = 0,
        tcp_rmem_min = 4096,
        accept_ra_all = False,
        tcp_adv_win_scale = 2,
        tcp_wmem_default = 4096,
        tcp_wmem_min = 4096,
        tcp_port_min = 1024,
        tcp_stdurg = False,
        tcp_port_max = 65535,
        tcp_fin_timeout = 60,
        tcp_no_metrics_save = False,
        tcp_dsack = True,
        tcp_mgmt_wmem = 32768,
        tcp_abort_on_overflow = False,
        tcp_frto = 0,
        tcp_mem_pressure = 32768,
        tcp_app_win = 31,
        ip_no_pmtu_disc = True,
        llm_hdr_gap = 8,
        tcp_max_orphans = 8192,
        accept_ra_default = False,
        tcp_syn_retries = 5,
        tcp_moderate_rcvbuf = 0,
        tcp_max_syn_backlog = 1024,
        tcp_mem_low = 24576,
        tcp_tw_rfc1323_strict = False,
        tcp_fack = True,
        tcp_retrans_collapse = True,
        inter_packet_granular_delay = 0.0,
        llm_hdr_gap_ns = 10,
        tcp_large_icwnd = 0,
        tcp_rmem_default = 4096,
        tcp_keepalive_probes = 9,
        tcp_mem_high = 49152,
        tcp_tw_reuse = False,
        delayed_acks_timeout = 0,
        tcp_vegas_gamma = 2,
        adjust_tcp_buffers = True,
        tcp_synack_retries = 5,
        tcp_timestamps = True,
        tcp_reordering = 3,
        rps_needed = False,
        tcp_sack = True,
        tcp_bic_fast_convergence = 1,
        tcp_bic_low_window = 14
)

    DNS_3 = IxLoad.new("ixNetDnsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = DNS_3
)

    

    DNS_3.hostList.clear()

    

    DNS_3.searchList.clear()

    

    DNS_3.nameServerList.clear()

    

    DNS_3.config(
        domain = "",
        _Stale = False,
        itemType = "DnsPlugin",
        timeout = 30
)

    SCTP_3 = IxLoad.new("ixNetSctpPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = SCTP_3
)

    

    SCTP_3.config(
        useMultiHomingTar = False,
        heartbeatInterval = 30,
        maxInitRetrans = 8,
        betaRTO = 2,
        itemType = "SctpPlugin",
        initialRTO = 3,
        maxPathRetrans = 5,
        minRTO = 1,
        _Stale = False,
        alphaRTO = 3,
        cookieLife = 60,
        maxRTO = 60,
        maxAssocRetrans = 10,
        maxBurst = 4,
        heartbeatMaxBurst = 1000
)

    Meshing_5 = IxLoad.new("ixNetMeshingPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1.globalPlugins.appendItem(object = Meshing_5
)

    

    Meshing_5.trafficMaps.clear()

    

    HTTPClient1_Traffic2_HTTPServer1 = IxLoad.new("ixNetMeshingTrafficMap")

    # ixNet objects need to be added in the list before they are configured!
    Meshing_5.trafficMaps.appendItem(object = HTTPClient1_Traffic2_HTTPServer1
)

    

    HTTPClient1_Traffic2_HTTPServer1.config(
        ipPreference = 2,
        itemType = "MeshingTrafficMap",
        portRangesString = "",
        destinationActivityId = 0,
        _Stale = False,
        meshingType = 2,
        sourceActivityId = 0,
        configMapFilename = "HTTPClient1Script.configmap",
        name = "HTTPClient1!Traffic2_HTTPServer1"
)

    Meshing_5.config(
        _Stale = False,
        itemType = "MeshingPlugin"
)

    Network1.config(
        comment = "",
        name = "Network1",
        lineSpeed = "Default",
        aggregation = 0,
        portL1Settings = my_ixPortL1Settings
)

    Ethernet_3 = Network1.getL1Plugin()

    

    my_ixNetDataCenterSettings = IxLoad.new("ixNetDataCenterSettings")

    my_ixNetDataCenterSettings.dcPfcMapping.clear()

    

    my_ixNetDataCenterSettings.config(
        dcSupported = True,
        itemType = "DataCenterSettings",
        dcEnabled = False,
        dcPfcPauseDelay = 1,
        _Stale = False,
        dcMode = 2,
        dcPfcPauseEnable = False,
        dcFlowControl = 0
)

    my_ixNetEthernetELMPlugin = IxLoad.new("ixNetEthernetELMPlugin")

    my_ixNetEthernetELMPlugin.config(
        negotiationType = "master",
        _Stale = False,
        itemType = "EthernetELMPlugin",
        negotiateMasterSlave = True
)

    my_ixNetDualPhyPlugin = IxLoad.new("ixNetDualPhyPlugin")

    my_ixNetDualPhyPlugin.config(
        medium = "auto",
        _Stale = False,
        itemType = "DualPhyPlugin"
)

    Ethernet_3.childrenList.clear()

    

    MAC_VLAN_9 = IxLoad.new("ixNetL2EthernetPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Ethernet_3.childrenList.appendItem(object = MAC_VLAN_9
)

    

    MAC_VLAN_9.childrenList.clear()

    

    UP_IP_8 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_9.childrenList.appendItem(object = UP_IP_8
)

    

    UP_IP_8.childrenList.clear()

    

    eNodeB_2 = IxLoad.new("ixNetIxCatENodeBSimPlugin")

    # ixNet objects need to be added in the list before they are configured!
    UP_IP_8.childrenList.appendItem(object = eNodeB_2
)

    

    MAC_VLAN_11 = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_VLAN_11.childrenList.clear()

    

    CP_IP_10 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_11.childrenList.appendItem(object = CP_IP_10
)

    

    CP_IP_10.childrenList.clear()

    

    CP_IP_10.extensionList.clear()

    

    CP_IP_10.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_11.extensionList.clear()

    

    MAC_VLAN_11.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    User_Equipment_1 = IxLoad.new("ixNetIxCatENodeBSimUePlugin")

    User_Equipment_1.childrenList.clear()

    

    User_Equipment_1.extensionList.clear()

    

    User_Equipment_1.config(
        _Stale = False,
        itemType = "IxCatENodeBSimUePlugin"
)

    my_ixNetIxCatENodeBSimNetworkActivitySettings = IxLoad.new("ixNetIxCatENodeBSimNetworkActivitySettings")

    my_ixNetIxCatENodeBSimNetworkActivitySettings.config(
        implicitSynchronization = True,
        _Stale = False,
        itemType = "IxCatENodeBSimNetworkActivitySettings",
        implicitSynchronizationApnOnly = False
)

    my_ixNetIxCatENodeBSimNetworkActivity = IxLoad.new("ixNetIxCatENodeBSimNetworkActivity")

    my_ixNetIxCatENodeBSimNetworkActivity.config(
        _Stale = False,
        itemType = "IxCatENodeBSimNetworkActivity",
        activitySettings = my_ixNetIxCatENodeBSimNetworkActivitySettings
)

    MAC_GNB = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_GNB.childrenList.clear()

    

    IP_GNB = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_GNB.childrenList.appendItem(object = IP_GNB
)

    

    IP_GNB.childrenList.clear()

    

    IP_GNB.extensionList.clear()

    

    IP_GNB.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_GNB.extensionList.clear()

    

    MAC_GNB.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    eNodeB_2.childrenList.clear()

    

    eNodeB_2.extensionList.clear()

    

    eNodeB_2.config(
        _Stale = False,
        itemType = "IxCatENodeBSimPlugin",
        macPluginForCP = MAC_VLAN_11,
        uePlugin = User_Equipment_1,
        networkActivity = my_ixNetIxCatENodeBSimNetworkActivity,
        macPluginForGNB = MAC_GNB
)

    UP_IP_8.extensionList.clear()

    

    UP_IP_8.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_9.extensionList.clear()

    

    MAC_VLAN_9.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    Ethernet_3.extensionList.clear()

    

    Ethernet_3.config(
        advertise10Full = True,
        itemType = "L1EthernetPlugin",
        directedAddress = "01:80:C2:00:00:01",
        advertise5000Full = True,
        advertise2500Full = True,
        advertise100Half = True,
        autoNegotiate = True,
        _Stale = False,
        enableFlowControl = False,
        advertise10Half = True,
        speed = "k100FD",
        advertise10000Full = True,
        advertise1000Full = True,
        advertise100Full = True,
        dataCenter = my_ixNetDataCenterSettings,
        cardElm = my_ixNetEthernetELMPlugin,
        cardDualPhy = my_ixNetDualPhyPlugin
)

    #################################################
    # Setting the ranges starting with the plugins that need to be script gen first
    #################################################
    eNodeB_2.mmeRangeList.clear()

    MMEPool_R5 = IxLoad.new("ixNetIxCatENodeBSimMMERange")

    # ixNet objects need to be added in the list before they are configured.
    eNodeB_2.mmeRangeList.appendItem(object = MMEPool_R5
)

    

    MMEPool_R5.config(
        mmeCount = 1,
        itemType = "IxCatENodeBSimMMERange",
        mmeIpType = "IPv4",
        enabled = True,
        publishStats = False,
        mmePort = 36412,
        _Stale = False,
        mmeIP = "4.22.0.20",
        distributePerPort = False
)

    eNodeB_2.homeEnodebGatewayIpRangeList.clear()

    eNodeB_2.x2enodebRangeList.clear()

    eNodeB_2.enodebRangeList.clear()

    eNB_R5 = IxLoad.new("ixNetIxCatENodeBSimRange")

    # ixNet objects need to be added in the list before they are configured.
    eNodeB_2.enodebRangeList.appendItem(object = eNB_R5
)

    

    my_ixNetIxCatENodeBSimResourceStatusReport = IxLoad.new("ixNetIxCatENodeBSimResourceStatusReport")

    my_ixNetIxCatENodeBSimResourceStatusReport.config(
        resourceStatusReportDuration = 10,
        enableHWResourceStatusReport = True,
        itemType = "IxCatENodeBSimResourceStatusReport",
        requestS1ResourceStatusReport = True,
        requestRadioResourceStatusReport = True,
        ulS1ReportResponse = "0",
        enableResourceStatusReportRequests = False,
        absPatternTypeIsFDD = True,
        dlS1ReportResponse = "0",
        absReportPeriod = "3",
        enableResourceStatusReporting = False,
        requestABSResourceStatusReport = True,
        enableCompositeAvailableCapacityResourceStatusReport = True,
        enableS1ResourceStatusReport = True,
        enableABSstatusResourceStatusReport = True,
        s1ReportPeriod = "3",
        resourceStatusReportDelay = 5,
        _Stale = False,
        resourceStatusReportTimeBetweenReports = 1,
        compReportPeriod = "3",
        ulCompositeAvailableCapacity = 10,
        dlHwReportResponse = "0",
        requestCompositeAvailCapacityResourceStatusReport = True,
        enableRadioResourceStatusReport = True,
        ulRadioNonGBRusage = 10,
        hwReportPeriod = "3",
        dlRadioNonGBRusage = 10,
        ulHwReportResponse = "0",
        AllowPartialResourceStatusReport = True,
        singleReportPeriod = "3",
        capacityClassValue = 10,
        enableSingleResourceStatusReport = True,
        dlCompositeAvailableCapacity = 10,
        requestHWResourceStatusReport = True,
        radioReportPeriod = "3",
        ulRadioGBRusage = 10,
        dlRadioGBRusage = 10,
        dlABSstatus = 10
)

    my_ixNetIxCatENodeBSimLoadIndication = IxLoad.new("ixNetIxCatENodeBSimLoadIndication")

    my_ixNetIxCatENodeBSimLoadIndication.config(
        enableNumberOfTimesForLoadIndication = False,
        loadIndicationNumberOfMessages = 1,
        loadIndicationTimeBetweenMessages = 5,
        itemType = "IxCatENodeBSimLoadIndication",
        _Stale = False,
        loadIndicationDelay = 5,
        enableLoadIndication = False
)

    eNB_R5.x2eNodeBList.clear()

    

    eNB_R5.mhList.clear()

    

    eNB_R5.mmePoolList.clear()

    

    my_ixNetIxCatENodeBSimMMEPoolEntry = IxLoad.new("ixNetIxCatENodeBSimMMEPoolEntry")

    # ixNet objects need to be added in the list before they are configured!
    eNB_R5.mmePoolList.appendItem(object = my_ixNetIxCatENodeBSimMMEPoolEntry
)

    

    my_ixNetIxCatENodeBSimMMEPoolEntry.config(
        _Stale = False,
        itemType = "IxCatENodeBSimMMEPoolEntry",
        nextMMEPool = MMEPool_R5
)

    eNB_R5.config(
        divisionMode = "0",
        homeMNC = "06",
        itemType = "IxCatENodeBSimRange",
        sharedMNC_1 = "",
        echoRequestT3 = 3,
        publishStats = False,
        enodebCount = 1,
        sharedMNC_2 = "",
        eNodebGroupIncrement = 256,
        globalIdType = "1",
        ulEARFCN = 0,
        _Stale = False,
        eUtranCellIdentifier = "1",
        eNodebGroupMembers = 64,
        startSubscriberId = 100,
        ulTransmissionBandwidth = "0",
        trackingAreaCode = "0201",
        s1SetupFailureTolerance = 0,
        dscpValue = 0,
        multiCell = False,
        enableEchoRequest = False,
        enableS1SetupFailureTolerance = False,
        dlEARFCN = 0,
        enableGrouping = False,
        homeMCC = "450",
        dlTransmissionBandwidth = "0",
        sharedMCC_1 = "",
        sharedMCC_2 = "",
        enabled = True,
        useDataIP = True,
        physicalCellIdentifier = 0,
        macroENodeBStartID = "14002",
        sctpPort = 36412,
        mlbResourceStatusReport = my_ixNetIxCatENodeBSimResourceStatusReport,
        loadIndication = my_ixNetIxCatENodeBSimLoadIndication
)

    IP_R10_CP = eNB_R5.getLowerRelatedRangeByIndex("IpV4V6Range", 0)

    IP_R10_CP.config(
        count = 1,
        enableGatewayArp = False,
        randomizeSeed = 4137179164,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = False,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "::1",
        prefix = 112,
        _Stale = False,
        gatewayIncrement = "::0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "::0",
        ipAddress = "::1400:1401",
        ipType = "IPv6"
)

    MAC_R9_CP = IP_R10_CP.getLowerRelatedRange("MacRange")

    MAC_R9_CP.config(
        count = 1,
        itemType = "MacRange",
        enabled = False,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:00:F2:22:60:B9",
        _Stale = False,
        mtu = 1500
)

    VLAN_R19_CP = IP_R10_CP.getLowerRelatedRange("VlanIdRange")

    VLAN_R19_CP.config(
        incrementStep = 1,
        innerIncrement = 1,
        uniqueCount = 4094,
        itemType = "VlanIdRange",
        tpid = "0x8100",
        idIncrMode = 2,
        enabled = False,
        innerFirstId = 1,
        increment = 1,
        priority = 1,
        _Stale = False,
        firstId = 1,
        innerTpid = "0x8100",
        innerIncrementStep = 1,
        innerUniqueCount = 4094,
        innerEnable = False,
        innerPriority = 1
)

    IP_R9_UP = eNB_R5.getLowerRelatedRangeByIndex("IpV4V6Range", 1)

    IP_R9_UP.config(
        count = 1,
        enableGatewayArp = False,
        randomizeSeed = 1187214632,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = True,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "0.0.0.1",
        prefix = 16,
        _Stale = False,
        gatewayIncrement = "0.0.0.0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "0.0.0.0",
        ipAddress = "4.22.0.10",
        ipType = "IPv4"
)

    MAC_R10_UP = IP_R9_UP.getLowerRelatedRange("MacRange")

    MAC_R10_UP.config(
        count = 1,
        itemType = "MacRange",
        enabled = True,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:16:00:0A:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R20_UP = IP_R9_UP.getLowerRelatedRange("VlanIdRange")

    VLAN_R20_UP.config(
        incrementStep = 1,
        innerIncrement = 1,
        uniqueCount = 4094,
        itemType = "VlanIdRange",
        tpid = "0x8100",
        idIncrMode = 2,
        enabled = False,
        innerFirstId = 1,
        increment = 1,
        priority = 1,
        _Stale = False,
        firstId = 1,
        innerTpid = "0x8100",
        innerIncrementStep = 1,
        innerUniqueCount = 4094,
        innerEnable = False,
        innerPriority = 1
)

    eNodeB_2.enodebUeRangeList.clear()

    UE_R21 = IxLoad.new("ixNetIxCatENodeBSimUeRange")

    # ixNet objects need to be added in the list before they are configured.
    eNodeB_2.enodebUeRangeList.appendItem(object = UE_R21
)

    

    my_ixNetIxCatENodeBSimCipheringAlgorithms = IxLoad.new("ixNetIxCatENodeBSimCipheringAlgorithms")

    my_ixNetIxCatENodeBSimCipheringAlgorithms.config(
        snow3gCipheringAlgorithm = True,
        aesCipheringAlgorithm = True,
        _Stale = False,
        itemType = "IxCatENodeBSimCipheringAlgorithms",
        nullCipheringAlgorithm = True
)

    my_ixNetIxCatENodeBSimUeFailureTesting = IxLoad.new("ixNetIxCatENodeBSimUeFailureTesting")

    my_ixNetIxCatENodeBSimUeFailureTesting.config(
        itemType = "IxCatENodeBSimUeFailureTesting",
        nasSecurityModeRejectIntegrityFailureRate = 100,
        enableNASSecurityModeRejectIntegrityFailure = False,
        s1ReselectionSRFailureRate = 100,
        enableHandoverCancelImmediately = False,
        enableS1ReselectionAttachFailure = False,
        s1ReselectionDetachFailureRate = 100,
        enableNASAuthenticationRejectMACFailure = False,
        nasAuthenticationRejectSyncFailureRate = 100,
        nasInformationRequestRetransmissionFailureRate = 100,
        s1ReselectionTAUFailureRate = 100,
        _Stale = False,
        enableNASInformationRequestRetransmission = False,
        enableS1ReselectionTAUFailure = False,
        handoverCancelImmediatelyFailureRate = 100,
        nasSecurityModeCommandRetransmissionFailureRate = 100,
        enableRejectHOFromTargeteNB = False,
        nasAuthenticationRejectMACFailureRate = 100,
        nasAuthenticationRequestRetransmissionFailureRate = 100,
        enableNASAuthenticationRejectSyncFailure = False,
        nasSecurityModeRejectCapabilitiesMismatchFailureRate = 100,
        s1ReselectionAttachFailureRate = 100,
        enableS1ReselectionSRFailure = False,
        rejectHOFromTargeteNBFailureRate = 100,
        enableNASAuthenticationRequestRetransmission = False,
        enableS1ReselectionDetachFailure = False,
        enableNASSecurityModeRejectCapabilitiesMismatch = False,
        enableCancelAfterHandoverPreparation = False,
        enableNASSecurityModeCommandRetransmission = False,
        cancelAfterHandoverPreparationFailureRate = 100
)

    my_ixNetIxCatENodeBSimUeNetworkCapabilityCIoT = IxLoad.new("ixNetIxCatENodeBSimUeNetworkCapabilityCIoT")

    my_ixNetIxCatENodeBSimUeNetworkCapabilityCIoT.config(
        upCIoT = False,
        s1uData = False,
        itemType = "IxCatENodeBSimUeNetworkCapabilityCIoT",
        cpCIoT = True,
        hccp = False,
        erWoPDN = False,
        _Stale = False
)

    my_ixNetIxCatENodeBSimIntegrityAlgorithms = IxLoad.new("ixNetIxCatENodeBSimIntegrityAlgorithms")

    my_ixNetIxCatENodeBSimIntegrityAlgorithms.config(
        aesIntegrityAlgorithm = True,
        snow3gIntegrityAlgorithm = True,
        _Stale = False,
        itemType = "IxCatENodeBSimIntegrityAlgorithms",
        nullIntegrityAlgorithm = True
)

    UE_R21.pcoList.clear()

    

    IxCatENodeBSimUePCO_7 = IxLoad.new("ixNetIxCatENodeBSimUePCO")

    # ixNet objects need to be added in the list before they are configured!
    UE_R21.pcoList.appendItem(object = IxCatENodeBSimUePCO_7
)

    

    my_ixNetIxCatRNCIuPSQoSv1 = IxLoad.new("ixNetIxCatRNCIuPSQoSv1")

    my_ixNetIxCatRNCIuPSQoSv1.config(
        reliabilityClass = 2,
        itemType = "IxCatRNCIuPSQoSv1",
        sduErrorRatio = 6,
        maxBitRateDLEx = 0,
        guaranteedBitRateUL = 64,
        maxSDUSize = 151,
        guaranteedBitRateDL = 64,
        signalingIndication = 0,
        _Stale = False,
        deliveryOrder = 2,
        delayClass = 0,
        maxBitRateULEx = 0,
        guaranteedBitRateULEx = 0,
        peakThroughput = 6,
        precedenceClass = 2,
        maxBitRateDL = 8640,
        trafficHandlingPriority = 1,
        guaranteedBitRateDLEx = 0,
        meanThroughput = 31,
        maxBitRateUL = 8640,
        transferDelay = 4000,
        trafficClass = 4,
        deliveryOfErroneousSDU = 1,
        sourceStatisticsDescriptor = 0,
        residualBER = 7
)

    my_ixNetIxCatENodeBSimApnEntry = IxLoad.new("ixNetIxCatENodeBSimApnEntry")

    my_ixNetIxCatENodeBSimApnEntry.qciList.clear()

    

    my_ixNetIxCatENodeBSimApnEntry.config(
        itemType = "IxCatENodeBSimApnEntry",
        updateAmbrIncrement = 10,
        apn = "ixiaint.lguplus.co.kr",
        arpPriorityLevel = 1,
        lifetime = 100,
        enablePCO = False,
        enablePCSCF = False,
        qciLabel = "Click to configure...",
        ipv6PrefixInPCO = True,
        arpPreemptionCapability = True,
        updateAmbrTimeout = 10,
        _Stale = False,
        qci = 9,
        option3xT3 = 5,
        enableLifetime = False,
        qosLabel = "Click to configure...",
        enableAmbrUpdate = False,
        updateAmbrIterations = 1,
        arpPreemptionVulnerability = True,
        ipType = "IPv4",
        mbru = 0,
        enabled = True,
        pcoProtocol = "PAP",
        mbrd = 0,
        emergencyApn = False,
        qosv1 = my_ixNetIxCatRNCIuPSQoSv1
)

    IxCatENodeBSimUePCO_7.config(
        authUserIdIncr = False,
        itemType = "IxCatENodeBSimUePCO",
        authCustomPCO = "8080211001000010810600000000830600000000000a00",
        authPasswordIncr = False,
        enabled = True,
        _Stale = False,
        authUserId = "user",
        authPassword = "password",
        apnEntry = my_ixNetIxCatENodeBSimApnEntry
)

    UE_R21.mobilityPathList.clear()

    

    UE_R21.config(
        enableMO = True,
        srvcc_mcc = "226",
        srvcc_rac = 100,
        itemType = "IxCatENodeBSimUeRange",
        edrxPagingTimeWindow = 0,
        srvcc_lac = 100,
        smsEnabled = False,
        mss = 1424,
        identityCycling = False,
        securityMnc = "03",
        publishStats = False,
        t3412extTimerUnit = 0,
        authOpValue = "112233445566778899AABBCCDDEEFF00",
        maxIntervalVariation = 0,
        imeiSWVer = "00",
        mnc = "06",
        authMode = "0",
        enableSRUD = False,
        periodicSRUDinterval = 5,
        pnb_ciot = "1",
        enableCIoT = False,
        smscNumber = "4070000000",
        edrxValue = 0,
        csfbTimeBetweenCalls = 60,
        emergencyAttach = False,
        identitiesOverrideListEnabled = False,
        psmTimerValue = 1,
        authOpcGlobal = "1918b840195c97017228127009ca194e",
        csfbTotalNumberOfCalls = 1,
        _Stale = False,
        msin = "1015000000",
        identitiesOverrideListFile = "Click to set...",
        startSubscriberId = 1,
        accessClass = "255",
        securityMcc = "312",
        msisdn = "4070000001",
        uesim_attachToPredefinedApn = False,
        enableMobility = False,
        enablePSMTimer = False,
        smsTypeOfNumber = "1",
        mcc = "450",
        requestT3412ext = False,
        t3412extTimerValue = 1,
        smsNumberPlanId = "1",
        imsiOnlyAttach = False,
        authKIncrement = 0,
        startDelay = 0,
        identityCount = 20,
        authKValue = "112233445566778899AABBCCDDEEFF00",
        maxDelayVariation = 0,
        imei = "12345678901234",
        psmTimerUnit = 1,
        srvccCapable = False,
        csfbStartDelay = 10,
        ignorePagingCount = 1,
        operationMode = "0",
        count = 1,
        enableCSFB = False,
        fragmentation = False,
        authOpcFile = "Click to set...",
        ipType = "IPv4",
        enableeDRX = False,
        uesim_testUSIM_TS34108 = False,
        csfbCallDuration = 60,
        enabled = True,
        smsMOEnabled = True,
        mobilityInterval = 60,
        smsTargetMSISDN = "4080000001",
        paging = "0",
        srvcc_nodeId = 1,
        srvcc_mnc = "10",
        uesim_ucs2 = "0",
        oneSRUDperProcedure = False,
        identityType = "0",
        enablePeriodicSRUD = False,
        cipheringAlgorithm = my_ixNetIxCatENodeBSimCipheringAlgorithms,
        ueFailureTesting = my_ixNetIxCatENodeBSimUeFailureTesting,
        parentRange = eNB_R5,
        ueNetworkCapability = my_ixNetIxCatENodeBSimUeNetworkCapabilityCIoT,
        integrityAlgorithm = my_ixNetIxCatENodeBSimIntegrityAlgorithms
)

    eNodeB_2.enbAssociationList.clear()

    

    #################################################
    # Creating the IP Distribution Groups
    #################################################
    Subscriber2_Network1.config(
        enable = True,
        tcpAccelerationAllowedFlag = True,
        network = Network1
)

    #################################################
    # Network Activities for Subscriber2@Network1
    #################################################
    Activity_eNB_S1_MME_CP = Subscriber2_Network1.networkActivityList.getNetworkActivityByPluginType(eNodeB_2, "Control Plane")

    #################################################
    # Timeline2 for activities HTTPClient1, eNB S1-MME CP
    #################################################
    Timeline2 = IxLoad.new("ixTimeline")

    Timeline2.config(
        rampUpValue = 1,
        offlineTime = 0,
        rampDownTime = 20,
        standbyTime = 0,
        rampDownValue = 0,
        iterations = 1,
        rampUpInterval = 1,
        sustainTime = 30,
        timelineType = 0,
        name = "Timeline2"
)

    Activity_eNB_S1_MME_CP.config(
        enable = True,
        timeline = Timeline2
)

    Activity_eNB_S1_MME_CP.agent.config(
        cmdListLoops = 0,
        flowPercentage = 100.0
)

    Activity_eNB_S1_MME_CP.agent.pm.commands.clear()

    Activity_eNB_S1_MME_CP.agent.pm.commands.appendItem(
        commandType = "NetworkCommand",
        subType = "enodebsimeNegativeTesting"
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[0].config(
        displayName = "Negative Testing",
        _Stale = False,
        itemType = "IxCatENodeBSimCommandNegativeTesting"
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[0].clear("nasNegativeTestingList")

    my_ixNetIxCatENodeBSimCommandNegativeTestingNasEntry = IxLoad.new("ixNetIxCatENodeBSimCommandNegativeTestingNasEntry")

    my_ixNetIxCatENodeBSimCommandNegativeTestingNasEntry.config(
        value = "178a7f32dd070741020bf654f06054f060810103d890f31805f0f0000010002d0201d0312726808021100100001081060000000083060000",
        _Stale = False,
        itemType = "IxCatENodeBSimCommandNegativeTestingNasEntry",
        messageType = 0,
        replacePacket = True
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[0].appendItem("nasNegativeTestingList", object = my_ixNetIxCatENodeBSimCommandNegativeTestingNasEntry
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[0].clear("s1apNegativeTestingList")

    my_ixNetIxCatENodeBSimCommandNegativeTestingS1apEntry = IxLoad.new("ixNetIxCatENodeBSimCommandNegativeTestingS1apEntry")

    my_ixNetIxCatENodeBSimCommandNegativeTestingS1apEntry.config(
        itemType = "IxCatENodeBSimCommandNegativeTestingS1apEntry",
        replacePacket = False,
        value = "178a7f32dd070741020bf654f06054f060810103d890f31805f0f0000010002d0201d0312726808021100100001081060000000083060000",
        _Stale = False,
        messageType = 10,
        ieNo = 1
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[0].appendItem("s1apNegativeTestingList", object = my_ixNetIxCatENodeBSimCommandNegativeTestingS1apEntry
)

    Activity_eNB_S1_MME_CP.agent.pm.commands.appendItem(
        commandType = "NetworkCommand",
        subType = "enodebsimCreateSession"
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[1].config(
        displayName = "Create Session",
        _Stale = False,
        itemType = "IxCatENodeBSimCommandCreateSession",
        apn = my_ixNetIxCatENodeBSimApnEntry
)

    Activity_eNB_S1_MME_CP.agent.pm.commands.appendItem(
        commandType = "THINK",
        minimumInterval = 99999999,
        maximumInterval = 99999999,
        cmdName = "Think 2"
)

    Activity_eNB_S1_MME_CP.agent.pm.commands.appendItem(
        commandType = "NetworkCommand",
        subType = "enodebsimDeleteSession"
)

    Activity_eNB_S1_MME_CP.agent.pm.commands[3].config(
        displayName = "Delete Session",
        detachSwitchOff = False,
        _Stale = False,
        itemType = "IxCatENodeBSimCommandDeleteSession",
        apn = my_ixNetIxCatENodeBSimApnEntry
)

    Activity_eNB_S1_MME_CP.setPrimaryObjectiveType("None")

    # Sub-activities are automatically added for each associated endpoint range
    Activity_eNB_S1_MME_CP_numSubActivities = Activity_eNB_S1_MME_CP.subActivities.indexCount()

    #################################################
    # Network Sub-activity for Range UE-R21
    #################################################
    SubActivity_UE_R21 = Activity_eNB_S1_MME_CP.subActivities.getItem(0)

    #################################################
    # Subscriber Activity HTTPClient1 of NetTraffic Subscriber2@Network1
    #################################################
    Subscriber_Activity_HTTPClient1 = Subscriber2_Network1.activityList.appendItem(protocolAndType = "HTTP Client"
)

    Subscriber_Activity_HTTPClient1.config(
        secondaryConstraintValue = 100,
        enable = True,
        name = "HTTPClient1",
        userIpMapping = "1:1",
        enableConstraint = False,
        timerGranularity = 100,
        secondaryEnableConstraint = False,
        constraintValue = 100,
        userObjectiveValue = 1,
        secondaryConstraintType = "TransactionRateConstraint",
        constraintType = "ConnectionRateConstraint",
        userObjectiveType = "simulatedUsers",
        destinationIpMapping = "Consecutive",
        timeline = Timeline2
)

    Subscriber_Activity_HTTPClient1.agent.profileList.clear()

    Subscriber_Activity_HTTPClient1.agent.actionList.clear()

    APN_1 = IxLoad.new("ixNetworkCommand")

    APN_1.config(subType = "egtpAPN"
)

    APN_1.config(
        usePredefinedQci = True,
        usePredefinedTft = True,
        displayName = "APN",
        itemType = "IxCatENodeBSimCommandAPN",
        mbru = 96,
        protocolName = "HTTP",
        tft = "3X0X03500050",
        defaultBearerFallback = True,
        networkInitiatedBearer = False,
        ignoreTFT = False,
        gbru = 96,
        mbrd = 96,
        _Stale = False,
        qci = 10,
        useDefaultBearer = True,
        gbrd = 96,
        apn = my_ixNetIxCatENodeBSimApnEntry
)

    APN_1.clear("bearerList")

    DedicatedBearer_2 = IxLoad.new("ixNetIxCatENodeBSimCommandAPNBearer")

    DedicatedBearer_2.config(
        function = "none",
        usePredefinedQci = True,
        itemType = "IxCatENodeBSimCommandAPNBearer",
        mbru = 96,
        name = "DedicatedBearer-2",
        tft = "3X0X03500050",
        defaultBearerFallback = True,
        networkInitiatedBearer = False,
        ignoreTFT = False,
        gbru = 96,
        mbrd = 96,
        _Stale = False,
        qci = 10,
        usePredefinedTft = True,
        gbrd = 96
)

    APN_1.appendItem("bearerList", object = DedicatedBearer_2
)

    Subscriber_Activity_HTTPClient1.agent.actionList.appendItem(object = APN_1
)

    

    my_ixHttpCommand = IxLoad.new("ixHttpCommand")

    my_ixHttpCommand.config(
        profile = -1,
        enableDi = 0,
        namevalueargs = "",
        useSsl = 0,
        pingFreq = 10,
        streamIden = 3,
        destination = "Traffic2_HTTPServer1:80",
        sendMD5ChkSumHeader = 0,
        windowSize = "65536",
        cmdName = "Get 3",
        method = -1,
        commandType = "GET",
        abort = "None",
        arguments = "",
        sslProfile = -1,
        pageObject = "/1b.html",
        sendingChunkSize = "None"
)

    Subscriber_Activity_HTTPClient1.agent.actionList.appendItem(object = my_ixHttpCommand
)

    

    Subscriber_Activity_HTTPClient1.agent.methodProfileList.clear()

    Subscriber_Activity_HTTPClient1.agent.sslProfileList.clear()

    Subscriber_Activity_HTTPClient1.agent.headerList.clear()

    my_ixHttpHeaderString = IxLoad.new("ixHttpHeaderString")

    my_ixHttpHeaderString.config(data = "Accept: */*"
)

    Subscriber_Activity_HTTPClient1.agent.headerList.appendItem(object = my_ixHttpHeaderString
)

    

    my_ixHttpHeaderString1 = IxLoad.new("ixHttpHeaderString")

    my_ixHttpHeaderString1.config(data = "Accept-Language: en-us"
)

    Subscriber_Activity_HTTPClient1.agent.headerList.appendItem(object = my_ixHttpHeaderString1
)

    

    my_ixHttpHeaderString2 = IxLoad.new("ixHttpHeaderString")

    my_ixHttpHeaderString2.config(data = "Accept-Encoding: gzip, deflate"
)

    Subscriber_Activity_HTTPClient1.agent.headerList.appendItem(object = my_ixHttpHeaderString2
)

    

    my_ixHttpHeaderString3 = IxLoad.new("ixHttpHeaderString")

    my_ixHttpHeaderString3.config(data = "User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
)

    Subscriber_Activity_HTTPClient1.agent.headerList.appendItem(object = my_ixHttpHeaderString3
)

    

    Subscriber_Activity_HTTPClient1.agent.ipMappingList.clear()

    Subscriber_Activity_HTTPClient1.agent.authProfileList.clear()

    Subscriber_Activity_HTTPClient1.agent.config(
        cmdListLoops = 0,
        ecCurve = 19,
        highPerfWithSU = 0,
        vlanPriority = 0,
        validateCertificate = 0,
        enableDecompressSupport = 0,
        exactTransactions = 0,
        enableHttpsProxy = 0,
        perHeaderPercentDist = 0,
        enableSsl = 0,
        enablePerConnCookieSupport = 0,
        cookieRejectProbability = 0.0,
        disableMacValidation = 0,
        enableUnidirectionalClose = 0,
        enableAuth = 0,
        enableMasterSecret = 0,
        enableECcurve = 0,
        httpsTunnel = "0.0.0.0",
        piggybackAck = 1,
        maxPersistentRequests = 1,
        enableEsm = 0,
        certificate = "",
        sequentialSessionReuse = 0,
        tcpFastOpen = 0,
        browserEmulationName = "Custom1",
        enableSslSendCloseNotify = 0,
        cookieJarSize = 10,
        dontUseUpgrade = 0,
        maxPipeline = 1,
        contentLengthDeviationTolerance = 0,
        caCert = "",
        maxSessions = 3,
        enableHttpProxy = 0,
        disableDnsResolutionCache = 0,
        enableTrafficDistributionForCC = 0,
        enableTos = 0,
        precedenceTOS = 0,
        ipPreference = 2,
        maxHeaderLen = 1024,
        flowPercentage = 100.0,
        maxStreams = 1,
        reliabilityTOS = 0,
        sslRecordSize = "16384",
        privateKey = "",
        commandTimeout = 600,
        enablemetaRedirectSupport = 0,
        delayTOS = 0,
        enableIntegrityCheckSupport = 0,
        commandTimeout_ms = 0,
        privateKeyPassword = "",
        urlStatsCount = 10,
        followHttpRedirects = 0,
        tcpCloseOption = 0,
        enableVlanPriority = 0,
        esm = 1460,
        httpVersion = 0,
        enablesslRecordSize = 0,
        sslReuseMethod = 0,
        sslVersion = 3,
        enableLargeHeader = 0,
        throughputTOS = 0,
        enableCookieSupport = 0,
        enableConsecutiveIpsPerSession = 0,
        clientCiphers = "DEFAULT",
        enableHttpsTunnel = 0,
        enableAchieveCCFirst = 0,
        tos = 0,
        httpProxy = "0.0.0.0",
        keepAlive = 0,
        enableCRCCheckSupport = 0,
        httpsProxy = "0.0.0.0"
)

    Subscriber_Activity_HTTPClient1.agent.cmdPercentagePool.percentageCommandList.clear()

    Subscriber_Activity_HTTPClient1.agent.cmdPercentagePool.config(seed = 1
)

    Subscriber2_Network1.traffic.config(name = "Subscriber2"
)

    Subscriber2_Network1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeThroughputAcceleration, False)

    Subscriber2_Network1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeFCoEOffload, True)

    Subscriber2_Network1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeBPS, True)

    Subscriber2_Network1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeL23, True)

    Subscriber2_Network1.setTcpAccelerationAllowed(IxLoad.ixAgent.kTcpAcceleration, True)

    Subscriber2_Network1.setShowActualCPUUtilizationModeAllowed(False)

    Originate.elementList.appendItem(object = Subscriber2_Network1
)

    

    Originate.config(name = "Originate"
)

    Scenario1.columnList.appendItem(object = Originate
)

    

    DUT = IxLoad.new("ixTrafficColumn")

    DUT.elementList.clear()

    DUT.config(name = "DUT"
)

    Scenario1.columnList.appendItem(object = DUT
)

    

    Terminate = IxLoad.new("ixTrafficColumn")

    Terminate.elementList.clear()

    #################################################
    # Create ScenarioElement kNetTraffic
    #################################################
    Traffic2_Network3 = scenarioElementFactory.create(IxLoad.ixScenarioElementType.kNetTraffic)

    

    my_ixPortL2 = IxLoad.new("ixPortL1Settings")

    my_ixPortL2.config(
        useIEEEDefaults = True,
        requestRSFEC = False,
        autoNegotiate = False,
        enableRSFECStatistics = False,
        fecValue = 3,
        advertiseRSFEC = False,
        requestFCFEC = False,
        enableRSFEC = False,
        advertiseFCFEC = False
)

    #################################################
    # Network Network3 of NetTraffic Traffic2@Network3
    #################################################
    Network3 = Traffic2_Network3.cget("network")

    Network3.portList.appendItem(
        chassisId = 1,
        cardId = 2,
        portId = 1
)

    Network3.globalPlugins.clear()

    

    Settings_5 = IxLoad.new("ixNetIxLoadSettingsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = Settings_5
)

    

    Settings_5.config(
        teardownInterfaceWithUser = False,
        _Stale = False,
        itemType = "IxLoadSettingsPlugin",
        interfaceBehavior = 0
)

    Filter_5 = IxLoad.new("ixNetFilterPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = Filter_5
)

    

    Filter_5.config(
        all = False,
        pppoecontrol = False,
        isis = False,
        itemType = "FilterPlugin",
        auto = True,
        udp = "",
        tcp = "",
        mac = "",
        _Stale = False,
        pppoenetwork = False,
        ip = "",
        icmp = ""
)

    GratARP_5 = IxLoad.new("ixNetGratArpPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = GratARP_5
)

    

    GratARP_5.config(
        itemType = "GratArpPlugin",
        forwardGratArp = False,
        enabled = True,
        maxFramesPerSecond = 0,
        _Stale = False,
        rateControlEnabled = False
)

    TCP_5 = IxLoad.new("ixNetTCPPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = TCP_5
)

    

    TCP_5.config(
        tcp_bic = 0,
        tcp_tw_recycle = True,
        tcp_retries2 = 5,
        itemType = "TCPPlugin",
        disable_min_max_buffer_size = True,
        tcp_retries1 = 3,
        tcp_keepalive_time = 7200,
        tcp_mgmt_rmem = 87380,
        tcp_rfc1337 = False,
        tcp_ipfrag_time = 30,
        tcp_rto_max = 120000,
        tcp_window_scaling = False,
        delayed_acks = True,
        udp_port_randomization = False,
        tcp_vegas_alpha = 2,
        tcp_vegas_beta = 6,
        tcp_wmem_max = 262144,
        tcp_ecn = False,
        tcp_westwood = 0,
        tcp_rto_min = 200,
        delayed_acks_segments = 0,
        tcp_vegas_cong_avoid = 0,
        tcp_keepalive_intvl = 75,
        tcp_rmem_max = 262144,
        tcp_orphan_retries = 0,
        bestPerfSettings = False,
        tcp_max_tw_buckets = 180000,
        _Stale = False,
        tcp_low_latency = 0,
        tcp_rmem_min = 4096,
        accept_ra_all = False,
        tcp_adv_win_scale = 2,
        tcp_wmem_default = 4096,
        tcp_wmem_min = 4096,
        tcp_port_min = 1024,
        tcp_stdurg = False,
        tcp_port_max = 65535,
        tcp_fin_timeout = 60,
        tcp_no_metrics_save = False,
        tcp_dsack = True,
        tcp_mgmt_wmem = 32768,
        tcp_abort_on_overflow = False,
        tcp_frto = 0,
        tcp_mem_pressure = 32768,
        tcp_app_win = 31,
        ip_no_pmtu_disc = True,
        llm_hdr_gap = 8,
        tcp_max_orphans = 8192,
        accept_ra_default = False,
        tcp_syn_retries = 5,
        tcp_moderate_rcvbuf = 0,
        tcp_max_syn_backlog = 1024,
        tcp_mem_low = 24576,
        tcp_tw_rfc1323_strict = False,
        tcp_fack = True,
        tcp_retrans_collapse = True,
        inter_packet_granular_delay = 0.0,
        llm_hdr_gap_ns = 10,
        tcp_large_icwnd = 0,
        tcp_rmem_default = 4096,
        tcp_keepalive_probes = 9,
        tcp_mem_high = 49152,
        tcp_tw_reuse = False,
        delayed_acks_timeout = 0,
        tcp_vegas_gamma = 2,
        adjust_tcp_buffers = True,
        tcp_synack_retries = 5,
        tcp_timestamps = True,
        tcp_reordering = 3,
        rps_needed = False,
        tcp_sack = True,
        tcp_bic_fast_convergence = 1,
        tcp_bic_low_window = 14
)

    DNS_5 = IxLoad.new("ixNetDnsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = DNS_5
)

    

    DNS_5.hostList.clear()

    

    DNS_5.searchList.clear()

    

    DNS_5.nameServerList.clear()

    

    DNS_5.config(
        domain = "",
        _Stale = False,
        itemType = "DnsPlugin",
        timeout = 30
)

    SCTP_5 = IxLoad.new("ixNetSctpPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = SCTP_5
)

    

    SCTP_5.config(
        useMultiHomingTar = False,
        heartbeatInterval = 30,
        maxInitRetrans = 8,
        betaRTO = 2,
        itemType = "SctpPlugin",
        initialRTO = 3,
        maxPathRetrans = 5,
        minRTO = 1,
        _Stale = False,
        alphaRTO = 3,
        cookieLife = 60,
        maxRTO = 60,
        maxAssocRetrans = 10,
        maxBurst = 4,
        heartbeatMaxBurst = 1000
)

    Meshing_4 = IxLoad.new("ixNetMeshingPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network3.globalPlugins.appendItem(object = Meshing_4
)

    

    Meshing_4.trafficMaps.clear()

    

    Meshing_4.config(
        _Stale = False,
        itemType = "MeshingPlugin"
)

    Network3.config(
        comment = "",
        name = "Network3",
        lineSpeed = "Default",
        aggregation = 0,
        portL1Settings = my_ixPortL2
)

    Ethernet_5 = Network3.getL1Plugin()

    

    my_ixNetDataCenterSettings1 = IxLoad.new("ixNetDataCenterSettings")

    my_ixNetDataCenterSettings1.dcPfcMapping.clear()

    

    my_ixNetDataCenterSettings1.config(
        dcSupported = True,
        itemType = "DataCenterSettings",
        dcEnabled = False,
        dcPfcPauseDelay = 1,
        _Stale = False,
        dcMode = 2,
        dcPfcPauseEnable = False,
        dcFlowControl = 0
)

    my_ixNetEthernetELMPlugin1 = IxLoad.new("ixNetEthernetELMPlugin")

    my_ixNetEthernetELMPlugin1.config(
        negotiationType = "master",
        _Stale = False,
        itemType = "EthernetELMPlugin",
        negotiateMasterSlave = True
)

    my_ixNetDualPhyPlugin1 = IxLoad.new("ixNetDualPhyPlugin")

    my_ixNetDualPhyPlugin1.config(
        medium = "auto",
        _Stale = False,
        itemType = "DualPhyPlugin"
)

    Ethernet_5.childrenList.clear()

    

    MAC_VLAN_16 = IxLoad.new("ixNetL2EthernetPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Ethernet_5.childrenList.appendItem(object = MAC_VLAN_16
)

    

    MAC_VLAN_16.childrenList.clear()

    

    UP_IP_15 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_16.childrenList.appendItem(object = UP_IP_15
)

    

    UP_IP_15.childrenList.clear()

    

    MME_3 = IxLoad.new("ixNetIxCatMMEPlugin")

    # ixNet objects need to be added in the list before they are configured!
    UP_IP_15.childrenList.appendItem(object = MME_3
)

    

    MAC_VLAN_17 = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_VLAN_17.childrenList.clear()

    

    CP_IP_16 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_17.childrenList.appendItem(object = CP_IP_16
)

    

    CP_IP_16.childrenList.clear()

    

    CP_IP_16.extensionList.clear()

    

    CP_IP_16.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_17.extensionList.clear()

    

    MAC_VLAN_17.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    PCRF_HSS_3 = IxLoad.new("ixNetIxCatMMEPluginPcrf")

    PCRF_HSS_3.childrenList.clear()

    

    PCRF_HSS_3.extensionList.clear()

    

    PCRF_HSS_3.config(
        _Stale = False,
        itemType = "IxCatMMEPluginPcrf"
)

    MAC_VLAN_18 = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_VLAN_18.childrenList.clear()

    

    IP_17 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_18.childrenList.appendItem(object = IP_17
)

    

    IP_17.childrenList.clear()

    

    IP_17.extensionList.clear()

    

    IP_17.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_18.extensionList.clear()

    

    MAC_VLAN_18.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    MME_3.childrenList.clear()

    

    MME_3.extensionList.clear()

    

    MME_3.config(
        _Stale = False,
        itemType = "IxCatMMEPlugin",
        macPluginForCP = MAC_VLAN_17,
        pcrfPlugin = PCRF_HSS_3,
        macPluginForPassthrough = MAC_VLAN_18
)

    UP_IP_15.extensionList.clear()

    

    UP_IP_15.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_16.extensionList.clear()

    

    MAC_VLAN_16.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    Ethernet_5.extensionList.clear()

    

    Ethernet_5.config(
        advertise10Full = True,
        itemType = "L1EthernetPlugin",
        directedAddress = "01:80:C2:00:00:01",
        advertise5000Full = True,
        advertise2500Full = True,
        advertise100Half = True,
        autoNegotiate = True,
        _Stale = False,
        enableFlowControl = False,
        advertise10Half = True,
        speed = "k100FD",
        advertise10000Full = True,
        advertise1000Full = True,
        advertise100Full = True,
        dataCenter = my_ixNetDataCenterSettings1,
        cardElm = my_ixNetEthernetELMPlugin1,
        cardDualPhy = my_ixNetDualPhyPlugin1
)

    #################################################
    # Setting the ranges starting with the plugins that need to be script gen first
    #################################################
    CP_IP_16.rangeList.clear()

    IP_R15_CP = IxLoad.new("ixNetIpV4V6Range")

    # ixNet objects need to be added in the list before they are configured.
    CP_IP_16.rangeList.appendItem(object = IP_R15_CP
)

    

    IP_R15_CP.config(
        count = 1,
        enableGatewayArp = False,
        randomizeSeed = 3108774400,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = False,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "::1",
        prefix = 112,
        _Stale = False,
        gatewayIncrement = "::0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "::0",
        ipAddress = "::1400:2801",
        ipType = "IPv6"
)

    MAC_R14_CP = IP_R15_CP.getLowerRelatedRange("MacRange")

    MAC_R14_CP.config(
        count = 1,
        itemType = "MacRange",
        enabled = False,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:00:F8:EF:12:84",
        _Stale = False,
        mtu = 1500
)

    VLAN_R34_CP = IP_R15_CP.getLowerRelatedRange("VlanIdRange")

    VLAN_R34_CP.config(
        incrementStep = 1,
        innerIncrement = 1,
        uniqueCount = 4094,
        itemType = "VlanIdRange",
        tpid = "0x8100",
        idIncrMode = 2,
        enabled = False,
        innerFirstId = 1,
        increment = 1,
        priority = 1,
        _Stale = False,
        firstId = 1,
        innerTpid = "0x8100",
        innerIncrementStep = 1,
        innerUniqueCount = 4094,
        innerEnable = False,
        innerPriority = 1
)

    IP_17.rangeList.clear()

    MME_3.mmeRangeList.clear()

    MME_R4 = IxLoad.new("ixNetIxCatMMERange")

    # ixNet objects need to be added in the list before they are configured.
    MME_3.mmeRangeList.appendItem(object = MME_R4
)

    

    MME_R4.mhList.clear()

    

    MME_R4.config(
        enableMMEPSMTimer = False,
        itemType = "IxCatMMERange",
        mmeMNC = "10",
        publishStats = False,
        mmeGroup = 1,
        capacity = 1,
        resetTimer = 60,
        enableDDN = False,
        mmeCode = 1,
        _Stale = False,
        resetStartDelay = 10,
        startSubscriberId = 100,
        useDataIP = True,
        mmeMCC = "226",
        enableResets = False,
        mmePSMTimerValue = 1,
        dscpValue = 0,
        resetType = "1",
        count = 1,
        enableeDRX = False,
        resetCount = 1,
        enabled = True,
        dDNTimeout = 20,
        enablePSM = False,
        mmePSMTimerUnit = 1,
        sctpPort = 36412
)

    IP_R14_UP = MME_R4.getLowerRelatedRangeByIndex("IpV4V6Range", 1)

    IP_R14_UP.config(
        count = 1,
        enableGatewayArp = False,
        randomizeSeed = 798639098,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = True,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "0.0.0.1",
        prefix = 16,
        _Stale = False,
        gatewayIncrement = "0.0.0.0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "0.0.0.0",
        ipAddress = "4.22.0.20",
        ipType = "IPv4"
)

    MAC_R15_UP = IP_R14_UP.getLowerRelatedRange("MacRange")

    MAC_R15_UP.config(
        count = 1,
        itemType = "MacRange",
        enabled = True,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:16:00:14:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R35_UP = IP_R14_UP.getLowerRelatedRange("VlanIdRange")

    VLAN_R35_UP.config(
        incrementStep = 1,
        innerIncrement = 1,
        uniqueCount = 4094,
        itemType = "VlanIdRange",
        tpid = "0x8100",
        idIncrMode = 2,
        enabled = False,
        innerFirstId = 1,
        increment = 1,
        priority = 1,
        _Stale = False,
        firstId = 1,
        innerTpid = "0x8100",
        innerIncrementStep = 1,
        innerUniqueCount = 4094,
        innerEnable = False,
        innerPriority = 1
)

    MME_3.apnRangeList.clear()

    PCRF_R3 = IxLoad.new("ixNetIxCatMMEApnRange")

    # ixNet objects need to be added in the list before they are configured.
    MME_3.apnRangeList.appendItem(object = PCRF_R3
)

    

    my_ixNetIxCatServerQoSv1 = IxLoad.new("ixNetIxCatServerQoSv1")

    my_ixNetIxCatServerQoSv1.config(
        reliabilityClass = 2,
        itemType = "IxCatServerQoSv1",
        sduErrorRatio = 6,
        maxBitRateDLEx = 0,
        guaranteedBitRateUL = 64,
        maxSDUSize = 151,
        guaranteedBitRateDL = 64,
        signalingIndication = 0,
        _Stale = False,
        deliveryOrder = 2,
        delayClass = 0,
        maxBitRateULEx = 0,
        guaranteedBitRateULEx = 0,
        peakThroughput = 6,
        precedenceClass = 2,
        maxBitRateDL = 8640,
        trafficHandlingPriority = 1,
        guaranteedBitRateDLEx = 0,
        meanThroughput = 31,
        maxBitRateUL = 8640,
        transferDelay = 4000,
        trafficClass = 4,
        deliveryOfErroneousSDU = 1,
        sourceStatisticsDescriptor = 0,
        residualBER = 7
)

    PCRF_R3.pdpContextsList.clear()

    

    PCRF_R3.bearerList.clear()

    

    Bearer_R3 = IxLoad.new("ixNetIxCatMMEDedicatedBearers")

    # ixNet objects need to be added in the list before they are configured!
    PCRF_R3.bearerList.appendItem(object = Bearer_R3
)

    

    Bearer_R3.config(
        qosUpdateValue = 10,
        enableLifetime = False,
        itemType = "IxCatMMEDedicatedBearers",
        mbru = 65535,
        priorityLevel = 1,
        gbru = 65535,
        timeoutAction = "kDelete",
        apnAmbrUpdateValue = 0,
        enabled = True,
        tft = "3X0X03500050",
        mbrd = 65535,
        preemptionCapability = True,
        _Stale = False,
        mode = "kMsInitiated",
        lifetime = 10,
        custom_tft = "3X0X03500051",
        qci = 12,
        qosLabel = "Deprecated",
        preemptionVulnerability = True,
        gbrd = 65535
)

    PCRF_R3.config(
        qci = 9,
        itemType = "IxCatMMEApnRange",
        pCSCFIpv4Primary = "20.0.0.1",
        ambru = 75000,
        pCSCFIpType = "0",
        apn = "ixiaint.lguplus.co.kr",
        pCSCFIpv4Secondary = "20.0.0.2",
        secondaryPDPContextDelay = 1,
        lifetime = 10,
        ambrd = 150000,
        acceptEmergencyServices = False,
        mss = 1424,
        poolSize = 1,
        enableIMSApn = False,
        enableDedicatedBearerDelay = False,
        _Stale = False,
        ipv6PrefixIncrBy = "::1",
        pCSCFIpv6Primary = "::10.10.10.1",
        pCSCFIpv6Secondary = "::10.10.10.2",
        preemptionVulnerability = False,
        ipv6PrefixStartValue = "00C0:00FF:00EE:0000",
        enableLifetime = False,
        priorityLevel = 1,
        qosLabel = "Deprecated",
        poolStartIPv4 = "172.16.0.1",
        fakeQoS = "Click to set...",
        preemptionCapability = False,
        publishStats = False,
        defaultAPN = False,
        totalL7ServerCount = 1,
        ipv6PrefixIncrEvery = 1,
        poolStartIPv6 = "BEEF::AC10:65",
        l7ServerCount = 1,
        ipType = "IPv4",
        mbru = 75000,
        enabled = True,
        roundRobinDistribution = False,
        l7ServerIPv6 = "::1616:1616",
        ipv6PrefixEnable = False,
        l7ServerIPv4 = "22.22.22.22",
        mbrd = 150000,
        fragmentation = False,
        dedicatedBearerDelay = 1,
        enableSecondaryPDPContextDelay = False,
        qosv1 = my_ixNetIxCatServerQoSv1
)

    MME_3.ueRangeList.clear()

    UE_R23 = IxLoad.new("ixNetIxCatMMEUeRange")

    # ixNet objects need to be added in the list before they are configured.
    MME_3.ueRangeList.appendItem(object = UE_R23
)

    

    UE_R23.ueApnList.clear()

    

    my_ixNetIxCatServerUeApnEntryBase = IxLoad.new("ixNetIxCatServerUeApnEntryBase")

    # ixNet objects need to be added in the list before they are configured!
    UE_R23.ueApnList.appendItem(object = my_ixNetIxCatServerUeApnEntryBase
)

    

    my_ixNetIxCatServerUeApnEntryBase.config(
        _Stale = False,
        itemType = "IxCatServerUeApnEntryBase",
        nextApn = PCRF_R3
)

    UE_R23.config(
        rand = "112233445566778899AABBCCDDEEFF00",
        itemType = "IxCatMMEUeRange",
        hsst3412extTimerValue = 1,
        hssedrxPagingTimeWindow = 0,
        publishStats = False,
        enablePTmsiReallocation = False,
        enableNetworkSlicing = False,
        hssEnableeDRX = False,
        enableSecurity = True,
        authMode = "0",
        hsst3412extTimerUnit = 0,
        hssedrxValue = 0,
        ueMSISDN = "1234567890",
        authOP = "112233445566778899AABBCCDDEEFF00",
        integrityAlgorithm = "0",
        hssEnableT3412ext = False,
        ueCount = 1,
        createBearersOnAttach = False,
        t3412TimerUnit = 2,
        smsNumberPlanId = "1",
        ueMNC = "06",
        _Stale = False,
        enforcePSMeDRXTimers = True,
        traceInterfaces = "0",
        sqn = "123456789ABC",
        enableTrace = 0,
        startSubscriberId = 1,
        smsTypeOfNumber = "1",
        unRegistered = False,
        hssPSMTimerValue = 1,
        enableTraceAfterAttach = False,
        dedicatedMmeRange = "0",
        authOPc = "1918b840195c97017228127009ca194e",
        amf = "8000",
        t3412TimerValue = 9,
        authKIncrement = 0,
        identityRequestType = "1",
        relocateSGWOnHandovers = False,
        pTmsiReallocationTimer = 30,
        enableTraceDuringAttach = False,
        traceDepth = "0",
        authK = "112233445566778899AABBCCDDEEFF00",
        hssPSMTimerUnit = 1,
        traceCollectionEntityIpAddress = "192.168.1.1",
        cipheringAlgorithm = "0",
        enabled = True,
        ignoreAuthOnEmgAttach = False,
        hssEnablePSMTimer = False,
        ueMCC = "450",
        ueMSIN = "1000000001",
        piggybackBearersOnAttach = False
)

    #################################################
    # Creating the IP Distribution Groups
    #################################################
    Traffic2_Network3.config(
        enable = 1,
        tcpAccelerationAllowedFlag = True,
        network = Network3
)

    #################################################
    # Activity HTTPServer1 of NetTraffic Traffic2@Network3
    #################################################
    Activity_HTTPServer1 = Traffic2_Network3.activityList.appendItem(protocolAndType = "HTTP Server"
)

    _Match_Longest_ = IxLoad.new("ixMatchLongestTimeline")

    

    Activity_HTTPServer1.config(
        enable = True,
        name = "HTTPServer1",
        timeline = _Match_Longest_
)

    Activity_HTTPServer1.agent.webPageList.clear()

    _200_OK = IxLoad.new("ResponseHeader")

    _200_OK.responseList.clear()

    _200_OK.config(
        mimeType = "text/plain",
        expirationMode = 0,
        code = "200",
        dateIncrementFor = 1,
        name = "200_OK",
        lastModifiedMode = 1,
        lastModifiedIncrementEnable = False,
        enableCustomPutResponse = False,
        dateIncrementEnable = False,
        lastModifiedDateTimeValue = "2019/03/18 03:56:59",
        lastModifiedIncrementFor = 1,
        expirationAfterLastModifiedValue = 3600,
        dateTimeValue = "2019/03/18 03:56:59",
        dateZone = "GMT",
        dateMode = 2,
        expirationAfterRequestValue = 3600,
        dateIncrementBy = 5,
        expirationDateTimeValue = "2019/04/17 03:56:59",
        lastModifiedIncrementBy = 5,
        description = "OK"
)

    my_PageObject = IxLoad.new("PageObject")

    my_PageObject.config(
        chunkSize = "1",
        Md5Option = 3,
        payloadSize = "1-1",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/1b.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject
)

    

    my_PageObject1 = IxLoad.new("PageObject")

    my_PageObject1.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "4096-4096",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/4k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject1
)

    

    my_PageObject2 = IxLoad.new("PageObject")

    my_PageObject2.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "8192-8192",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/8k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject2
)

    

    my_PageObject3 = IxLoad.new("PageObject")

    my_PageObject3.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "16536-16536",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/16k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject3
)

    

    my_PageObject4 = IxLoad.new("PageObject")

    my_PageObject4.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "32768",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/32k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject4
)

    

    my_PageObject5 = IxLoad.new("PageObject")

    my_PageObject5.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "65536",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/64k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject5
)

    

    my_PageObject6 = IxLoad.new("PageObject")

    my_PageObject6.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "131072",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/128k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject6
)

    

    my_PageObject7 = IxLoad.new("PageObject")

    my_PageObject7.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "262144",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/256k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject7
)

    

    my_PageObject8 = IxLoad.new("PageObject")

    my_PageObject8.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "524288",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/512k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject8
)

    

    my_PageObject9 = IxLoad.new("PageObject")

    my_PageObject9.config(
        chunkSize = "512-1024",
        Md5Option = 3,
        payloadSize = "1048576",
        customPayloadId = -1,
        payloadType = "range",
        payloadFile = "<specify file>",
        page = "/1024k.html",
        response = _200_OK
)

    Activity_HTTPServer1.agent.webPageList.appendItem(object = my_PageObject9
)

    

    Activity_HTTPServer1.agent.cookieList.clear()

    UserCookie = IxLoad.new("CookieObject")

    UserCookie.cookieContentList.clear()

    firstName = IxLoad.new("ixCookieContent")

    firstName.config(
        domain = "",
        name = "firstName",
        maxAge = "",
        value = "Joe",
        other = "",
        path = ""
)

    UserCookie.cookieContentList.appendItem(object = firstName
)

    

    lastName = IxLoad.new("ixCookieContent")

    lastName.config(
        domain = "",
        name = "lastName",
        maxAge = "",
        value = "Smith",
        other = "",
        path = ""
)

    UserCookie.cookieContentList.appendItem(object = lastName
)

    

    UserCookie.config(
        mode = 3,
        type = 2,
        name = "UserCookie",
        description = "Name of User"
)

    Activity_HTTPServer1.agent.cookieList.appendItem(object = UserCookie
)

    

    LoginCookie = IxLoad.new("CookieObject")

    LoginCookie.cookieContentList.clear()

    name = IxLoad.new("ixCookieContent")

    name.config(
        domain = "",
        name = "name",
        maxAge = "",
        value = "joesmith",
        other = "",
        path = ""
)

    LoginCookie.cookieContentList.appendItem(object = name
)

    

    password = IxLoad.new("ixCookieContent")

    password.config(
        domain = "",
        name = "password",
        maxAge = "",
        value = "foobar",
        other = "",
        path = ""
)

    LoginCookie.cookieContentList.appendItem(object = password
)

    

    LoginCookie.config(
        mode = 2,
        type = 2,
        name = "LoginCookie",
        description = "Login name and password"
)

    Activity_HTTPServer1.agent.cookieList.appendItem(object = LoginCookie
)

    

    Activity_HTTPServer1.agent.customPayloadList.clear()

    AsciiCustomPayload = IxLoad.new("CustomPayloadObject")

    AsciiCustomPayload.config(
        repeat = 0,
        name = "AsciiCustomPayload",
        asciiPayloadValue = "Ixia-Ixload-Http-Server-Custom-Payload",
        payloadmode = 0,
        offset = 1,
        hexPayloadValue = "",
        payloadPosition = "Start With",
        id = 0
)

    Activity_HTTPServer1.agent.customPayloadList.appendItem(object = AsciiCustomPayload
)

    

    HexCustomPayload = IxLoad.new("CustomPayloadObject")

    HexCustomPayload.config(
        repeat = 0,
        name = "HexCustomPayload",
        asciiPayloadValue = "",
        payloadmode = 1,
        offset = 1,
        hexPayloadValue = "49 78 69 61 2d 49 78 6c 6f 61 64 2d 48 74 74 70 2d 53 65 72 76 65 72 2d 43 75 73 74 6f 6d 2d 50 61 79 6c 6f 61 64",
        payloadPosition = "Start With",
        id = 1
)

    Activity_HTTPServer1.agent.customPayloadList.appendItem(object = HexCustomPayload
)

    

    Activity_HTTPServer1.agent.responseHeaderList.clear()

    _201 = IxLoad.new("ResponseHeader")

    _201.responseList.clear()

    _201.config(
        mimeType = "text/plain",
        expirationMode = 0,
        code = "200",
        dateIncrementFor = 1,
        name = "200_OK",
        lastModifiedMode = 1,
        lastModifiedIncrementEnable = False,
        enableCustomPutResponse = False,
        dateIncrementEnable = False,
        lastModifiedDateTimeValue = "2019/03/18 03:56:59",
        lastModifiedIncrementFor = 1,
        expirationAfterLastModifiedValue = 3600,
        dateTimeValue = "2019/03/18 03:56:59",
        dateZone = "GMT",
        dateMode = 2,
        expirationAfterRequestValue = 3600,
        dateIncrementBy = 5,
        expirationDateTimeValue = "2019/04/17 03:56:59",
        lastModifiedIncrementBy = 5,
        description = "OK"
)

    Activity_HTTPServer1.agent.responseHeaderList.appendItem(object = _201
)

    

    _404_PageNotFound = IxLoad.new("ResponseHeader")

    _404_PageNotFound.responseList.clear()

    _404_PageNotFound.config(
        mimeType = "text/plain",
        expirationMode = 0,
        code = 404,
        dateIncrementFor = 1,
        name = "404_PageNotFound",
        lastModifiedMode = 1,
        lastModifiedIncrementEnable = False,
        enableCustomPutResponse = False,
        dateIncrementEnable = False,
        lastModifiedDateTimeValue = "2019/03/18 03:56:59",
        lastModifiedIncrementFor = 1,
        expirationAfterLastModifiedValue = 3600,
        dateTimeValue = "2019/03/18 03:56:59",
        dateZone = "GMT",
        dateMode = 2,
        expirationAfterRequestValue = 3600,
        dateIncrementBy = 5,
        expirationDateTimeValue = "2019/04/17 03:56:59",
        lastModifiedIncrementBy = 5,
        description = "Page not found"
)

    Activity_HTTPServer1.agent.responseHeaderList.appendItem(object = _404_PageNotFound
)

    

    Activity_HTTPServer1.agent.config(
        cmdListLoops = 0,
        vlanPriority = 0,
        validateCertificate = 0,
        maxResponseDelay = 0,
        docrootChunkSize = "512-1024",
        enableTls13Support = False,
        disableMacValidation = 0,
        rstTimeout = 100,
        enableChunkedRequest = False,
        enableEsm = 0,
        enableHTTP2 = False,
        certificate = "",
        enableNewSslSupport = False,
        tos = 0,
        enableSslSendCloseNotify = 0,
        enableMD5Checksum = False,
        httpPort = "80",
        httpsPort = "443",
        caCert = "",
        esm = 1460,
        enableTos = 0,
        precedenceTOS = 0,
        integrityCheckOption = "Custom MD5",
        flowPercentage = 100.0,
        enableChunkEncoding = False,
        privateKey = "",
        sslRecordSize = "16384",
        reliabilityTOS = 0,
        delayTOS = 0,
        privateKeyPassword = "",
        urlStatsCount = 10,
        tcpCloseOption = 0,
        enableVlanPriority = 0,
        enableIntegrityCheck = 0,
        docrootfile = "",
        enablesslRecordSize = 0,
        dhParams = "",
        throughputTOS = 0,
        requestTimeout = 300,
        dontExpectUpgrade = False,
        ServerCiphers = "DEFAULT",
        enableDHsupport = 0,
        enablePerServerPerURLstat = 0,
        urlPageSize = 1024,
        highPerfWithSU = 0,
        acceptSslConnections = 0,
        minResponseDelay = 0
)

    Traffic2_Network3.traffic.config(name = "Traffic2"
)

    Traffic2_Network3.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeThroughputAcceleration, False)

    Traffic2_Network3.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeFCoEOffload, True)

    Traffic2_Network3.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeBPS, True)

    Traffic2_Network3.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeL23, True)

    Traffic2_Network3.setTcpAccelerationAllowed(IxLoad.ixAgent.kTcpAcceleration, True)

    Traffic2_Network3.setShowActualCPUUtilizationModeAllowed(False)

    Terminate.elementList.appendItem(object = Traffic2_Network3
)

    

    Terminate.config(name = "Terminate"
)

    Scenario1.columnList.appendItem(object = Terminate
)

    

    Scenario1.appMixList.clear()

    Scenario1.links.clear()

    Scenario1.config(name = "Scenario1"
)

    Test1.config(
        comment = "",
        networkFailureThreshold = 0,
        statViewThroughputUnits = "Kbps",
        showNetworkDiagnosticsAfterRunStops = False,
        csvThroughputScalingFactor = 1000,
        enableReleaseConfigAfterRun = False,
        activitiesGroupedByObjective = False,
        resetNetworkDiagnosticsAtStartRun = True,
        enableForceNetworkUpdateCloud = False,
        enableFrameSizeDistributionStats = False,
        enableTcpAdvancedStats = False,
        showNetworkDiagnosticsFromApplyConfig = True,
        enableResetPorts = True,
        enableNetworkDiagnosticsLogging = True,
        csvInterval = 1,
        name = "Test1",
        downgradeAppLibFlowsToLatestValidVersion = True,
        statsRequired = True,
        isFrameSizeDistributionViewSupported = False,
        enableForceOwnership = True,
        enableNetworkDiagnostics = True,
        allowMixedObjectiveTypes = False,
        currentUniqueIDForAgent = 12,
        profileDirectory = profileDirectory,
        eventHandlerSettings = my_ixEventHandlerSettings,
        captureViewOptions = my_ixViewOptions
)

    #################################################
    # Destination HTTPServer1 for HTTPClient1
    #################################################
    destination = Subscriber2_Network1.getDestinationForActivity("HTTPClient1", "Traffic2_HTTPServer1")

    destination.config(portMapPolicy = "portPairs"
)

    #################################################
    # Session Specific Settings
    #################################################
    my_ixNetMacSessionData = Test1.getSessionSpecificData("L2EthernetPlugin")

    my_ixNetMacSessionData.config(
        _Stale = False,
        itemType = "MacSessionData",
        duplicateCheckingScope = 2
)

    my_ixNetIpSessionData = Test1.getSessionSpecificData("IpV4V6Plugin")

    my_ixNetIpSessionData.config(
        enableGatewayArp = False,
        itemType = "IpSessionData",
        ignoreUnresolvedIPs = False,
        individualARPTimeOut = 500,
        maxOutstandingGatewayArpRequests = 300,
        _Stale = False,
        sendAllRequests = False,
        gatewayArpRequestRate = 300,
        duplicateCheckingScope = 2
)

    my_ixNetIxCatENodeBSimPluginSessionData = Test1.getSessionSpecificData("IxCatENodeBSimPlugin")

    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.clear()

    

    my_ixNetIxCatENodeBSimQci2TosEntry = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci2TosEntry
)

    

    my_ixNetIxCatENodeBSimQci2TosEntry.config(
        tos = "10",
        qci = 1,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci3 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci3
)

    

    my_ixNetIxCatENodeBSimQci3.config(
        tos = "10",
        qci = 2,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci4 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci4
)

    

    my_ixNetIxCatENodeBSimQci4.config(
        tos = "10",
        qci = 3,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci5 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci5
)

    

    my_ixNetIxCatENodeBSimQci5.config(
        tos = "10",
        qci = 4,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci6 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci6
)

    

    my_ixNetIxCatENodeBSimQci6.config(
        tos = "10",
        qci = 5,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci7 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci7
)

    

    my_ixNetIxCatENodeBSimQci7.config(
        tos = "10",
        qci = 6,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci8 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci8
)

    

    my_ixNetIxCatENodeBSimQci8.config(
        tos = "10",
        qci = 7,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci9 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci9
)

    

    my_ixNetIxCatENodeBSimQci9.config(
        tos = "10",
        qci = 8,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimQci10 = IxLoad.new("ixNetIxCatENodeBSimQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatENodeBSimQci10
)

    

    my_ixNetIxCatENodeBSimQci10.config(
        tos = "10",
        qci = 9,
        enable = True,
        _Stale = False,
        itemType = "IxCatENodeBSimQci2TosEntry"
)

    my_ixNetIxCatENodeBSimPluginSessionData.config(
        enableGatewayArp = False,
        maxOutstandingRequests = 200,
        useMaxRatesForS1Setup = False,
        s1SetupMaxOutstanding = 300,
        itemType = "IxCatENodeBSimPluginSessionData",
        useMaxRatesForDcp = True,
        ignoreUnresolvedIPs = False,
        individualARPTimeOut = 500,
        validateHeNBLicense = False,
        enableDynamicQosCtrl = False,
        maxOutstandingReleases = 200,
        maxOutstandingGatewayArpRequests = 300,
        _Stale = False,
        sendAllRequests = False,
        setupRateInitial = 100,
        s1SetupRate = 300,
        teardownRateInitial = 100,
        gatewayArpRequestRate = 300,
        duplicateCheckingScope = 1
)

    my_ixNetIPSecSessionData = Test1.getSessionSpecificData("IPSecPlugin")

    my_ixNetIPSecCertificates = IxLoad.new("ixNetIPSecCertificates")

    my_ixNetIPSecCertificates.config(
        itemType = "IPSecCertificates",
        crlOverrideUrl = "",
        crlOverrideEnable = False,
        uniqueCert = False,
        checkCrl = False,
        certSubjectAltDN = "",
        keyGenAlgo = "RSA",
        bitSize = "k512",
        ocspOverrideEnable = False,
        saveCert = True,
        unknownIsRevoked = False,
        _Stale = False,
        caURL = "",
        certSource = "kNewCert",
        usePerRangeCertNameExp = False,
        ocspOverrideUrl = "",
        checkOcsp = False,
        remoteIkeId = "",
        lateExpDate = "",
        certProto = "kSCEP",
        certPath = "C:\\\\Program Files (x86)\\\\Ixia\\\\CachedCerts",
        certSubjectDN = "",
        certParentFolder = "C:\\\\Program Files (x86)\\\\Ixia\\\\CachedCerts",
        caDN = "",
        certificatesSource = "Get new certificates from CA",
        cacheCertFolder = "C:\\\\Program Files (x86)\\\\Ixia\\\\CachedCerts",
        caCertNumber = "",
        earlyExpDate = "",
        certNumber = "",
        keySize = "RSA - 512"
)

    my_ixNetIPSecCertManager = IxLoad.new("ixNetIPSecCertManager")

    my_ixNetIPSecCertManager.config(
        uniqueCert = False,
        useDescFile = False,
        itemType = "IPSecCertManager",
        keyGenAlgo = "kRSA_512_sha1",
        caCrtFile = "C:\\\\Program Files (x86)\\\\Ixia\\\\ca-cert.crt",
        cacheCertFolder = "C:\\\\Program Files (x86)\\\\Ixia\\\\CachedCerts",
        certProto = "kSCEP",
        _Stale = False,
        certSubjectDN = "CN=IxiaVPN,C=RO,L=Bucharest,O=Ixia",
        caURL = "",
        createRootCA = False,
        caKeyFile = "C:\\\\Program Files (x86)\\\\Ixia\\\\ca-priv.key",
        descFilePath = "C:\\\\Program Files (x86)\\\\Ixia\\\\CachedCerts\\\\sample.desc",
        caDN = "CN=RootCA,C=RO,L=Bucharest,O=Ixia,OU=IxLoad,IP:201.121.87.2,email:ixia@ixiacom.com",
        certNumber = 1
)

    my_ixNetIPSecTunnelSetup = IxLoad.new("ixNetIPSecTunnelSetup")

    my_ixNetIPSecTunnelSetup.config(
        retryInterval = 10,
        useMaxPendingTunnels = False,
        enableRekey = True,
        itemType = "IPSecTunnelSetup",
        logLevel = "3",
        testType = "P2D",
        rekeyRetries = 3,
        tunnelSetupTimeout = 30,
        retryDelay = 10,
        sendCiscoVid = False,
        rekeyMargin = 10,
        rekeyFuzzPercentage = 0,
        tunnelRetransmissionTimeout = 30,
        _Stale = False,
        numRetries = 0,
        useMaxInitiationRate = False
)

    my_ixNetIPSecSessionData.eapAkaTuples.clear()

    

    my_ixNetIPSecSessionData.payloadAttrTypes.clear()

    

    my_ixNetIPSecSessionData.eapSimTuples.clear()

    

    my_ixNetIPSecSessionData.config(
        enableWildcardTsi = False,
        itemType = "IPSecSessionData",
        maxInitiationRate = 50,
        parallelInitiation = False,
        negotiationStartDelay = 0,
        maxPendingTunnels = 50,
        burstInitiation = False,
        _Stale = False,
        enablePlutoS2SWildcardTsr = False,
        teardownRate = 10,
        enableWildcardTsr = False,
        enablePlutoModeCfgWildcardTsr = True,
        enablePlutoWildcardTsi = False,
        ipsecCertificates = my_ixNetIPSecCertificates,
        ipsecCertManager = my_ixNetIPSecCertManager,
        ipsecTunnelSetup = my_ixNetIPSecTunnelSetup
)

    my_ixNetIxCatMMEPluginSessionData = Test1.getSessionSpecificData("IxCatMMEPlugin")

    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.clear()

    

    my_ixNetIxCatMMEQci2TosEntry = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci2TosEntry
)

    

    my_ixNetIxCatMMEQci2TosEntry.config(
        tos = "10",
        qci = 1,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci3 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci3
)

    

    my_ixNetIxCatMMEQci3.config(
        tos = "10",
        qci = 2,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci4 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci4
)

    

    my_ixNetIxCatMMEQci4.config(
        tos = "10",
        qci = 3,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci5 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci5
)

    

    my_ixNetIxCatMMEQci5.config(
        tos = "10",
        qci = 4,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci6 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci6
)

    

    my_ixNetIxCatMMEQci6.config(
        tos = "10",
        qci = 5,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci7 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci7
)

    

    my_ixNetIxCatMMEQci7.config(
        tos = "10",
        qci = 6,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci8 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci8
)

    

    my_ixNetIxCatMMEQci8.config(
        tos = "10",
        qci = 7,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci9 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci9
)

    

    my_ixNetIxCatMMEQci9.config(
        tos = "10",
        qci = 8,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEQci10 = IxLoad.new("ixNetIxCatMMEQci2TosEntry")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatMMEPluginSessionData.qci2TosMap.appendItem(object = my_ixNetIxCatMMEQci10
)

    

    my_ixNetIxCatMMEQci10.config(
        tos = "10",
        qci = 9,
        enable = True,
        _Stale = False,
        itemType = "IxCatMMEQci2TosEntry"
)

    my_ixNetIxCatMMEPluginSessionData.config(
        enableGatewayArp = False,
        itemType = "IxCatMMEPluginSessionData",
        ignoreUnresolvedIPs = False,
        individualARPTimeOut = 500,
        maxOutstandingGatewayArpRequests = 300,
        _Stale = False,
        sendAllRequests = False,
        gatewayArpRequestRate = 300,
        validateHeNBGatewayLicense = False,
        duplicateCheckingScope = 1
)

    #################################################
    # Network Specific Settings(overrides some of the session specific settings)
    #################################################
    # If the 'override' property is set to true the specific settings for this network will override the session specific settings
    my_ixNetIxCatMMEPortGroupData = Network3.getNetworkSpecificData("IxCatMMEPlugin")

    my_ixNetIxCatMMEPortGroupData.activities.clear()

    

    my_ixNetIxCatMMEPortGroupData.associates.clear()

    

    my_ixNetIxCatMMEPortGroupData.config(
        csfbStartDelay = 10,
        smsTimeBetweenMessages = 60,
        customFailureField1 = False,
        enableSMS = False,
        doNotAuthenticateUE = False,
        cellBroadcastTotalNumberOfWarnings = 1,
        _4Gto3GHandoverFailure = False,
        milenage_r4 = 64,
        milenage_r5 = 96,
        milenage_r2 = 0,
        milenage_r3 = 32,
        milenage_r1 = 64,
        authenticationDuringTAU = False,
        smsTotalNumberOfMessages = 1,
        broadcastPaging = False,
        instanceCount = 1,
        x2HandoverFailure = False,
        pdnConnectReject = False,
        autoDetectInstances = True,
        papNak = False,
        errorIndication = False,
        s1ReleaseAfterDedicatedBearerEstablished = False,
        enableSecurityTracing = False,
        attachReject = False,
        emmCauseValue = 7,
        deleteAllNonEmergencyBearers = False,
        enableGtpuSequenceNumber = False,
        kasmeMismatch = False,
        abortSctpOnLinkUp = False,
        imsiPaging = False,
        abortSctpOnS1Setup = False,
        randomizeSctpAborts = False,
        s1HandoverFailure = False,
        adaptorLogLevel = "0",
        enableNasTracing = False,
        enableIPDefragmentation = False,
        bearerAllocationRetransmissionTimeout = False,
        esmCauseValue = 31,
        failureRate = 0,
        pcpuLogLevel = "0",
        enableCellBroadcast = False,
        useNullSecurity = False,
        s1ReleaseDuringDedicatedBearerEstablishedBeforeErabSetup = False,
        testAdditionalErabRelease = False,
        s1ReleaseDuringTAU = False,
        sendKillRequest = True,
        instanceIdStr = "obsolete",
        bearerModificationReject = False,
        numberOfPages = 1,
        bypassMaxBearersValidation = False,
        enableDeleteSessionsOneByOne = False,
        ignoreAttachRejectForEmergencyAttach = False,
        pdnConnectRetransmissionTimeout = False,
        itemType = "IxCatMMEPortGroupData",
        enableNetworkInitiatedDetach = False,
        pdnDisconnectRetransmissionTimeout = False,
        s1SetupFailure = False,
        displayLogLevel = "0",
        warningAreaType = "1",
        csfbTimeBetweenCalls = 60,
        _Stale = False,
        showMessageAnalyst = False,
        cellBroadcastTimeBetweenWarnings = 60,
        loopbackIotTraffic = False,
        testModifyIpv6Id = False,
        distributeUserPlaneIps = False,
        cellBroadcastWarningDuration = 10,
        s1SetupTimeToWait = "100",
        rejectNewSessionsIfEmergencySessionExists = False,
        useNullKenb = False,
        maxSctpAborts = 5,
        noS1ReleaseDuringIdleTAU = False,
        attachRetransmissionTimeout = False,
        duplicateDedicatedBearer = False,
        chapFailure = False,
        networkInitiatedDetachTimer = 100,
        enableMilenage = False,
        suppressGtpuErrorIndication = False,
        securityModeDuringTAU = False,
        tauReject = False,
        milenage_c2 = "00000000000000000000000000000001",
        enableAttachRemoteTeidGuessing = True,
        chapSuccess = False,
        enablePerUeStats = True,
        s1ReleaseDuringDedicatedBearerEstablishedAfterErabSetup = False,
        ddriverLogLevel = "0",
        detachRetransmissionTimeout = False,
        skipNasSecurityModeCommand = False,
        milenage_c1 = "00000000000000000000000000000000",
        milenage_c3 = "00000000000000000000000000000002",
        customTestValue = 0,
        milenage_c5 = "00000000000000000000000000000008",
        milenage_c4 = "00000000000000000000000000000004",
        tauRetransmissionTimeout = False,
        serviceRequestRetransmissionTimeout = False,
        cellBroadcastStartDelay = 20,
        linkFailure = False,
        csfbTotalNumberOfCalls = 1,
        serviceReject = False,
        _3Gto4GHandoverFailure = False,
        authenticateAllAttaches = False,
        srvccCapable = False,
        s1HandoverTimeout = False,
        emulateSrvccHandover = False,
        enableCSFB = False,
        s1SetupFailureRate = 0,
        bearerModificationRetransmissionTimeout = False,
        abortSctpAfterS1Setup = False,
        itpLogLevel = "0",
        smsStartDelay = 10
)

    # If the 'override' property is set to true the specific settings for this network will override the session specific settings
    my_ixNetIPSecPortGroupData = Network3.getNetworkSpecificData("IPSecPlugin")

    my_ixNetIPSecPortGroupData.activities.clear()

    

    my_ixNetIPSecPortGroupData.associates.clear()

    

    my_ixNetIPSecPortGroupData.config(
        useMaxPendingTunnels = False,
        itemType = "IPSecPortGroupData",
        enableESPPerStreamStats = False,
        maxInitiationRate = 50,
        enableESPReplayStats = False,
        maxPendingTunnels = 50,
        _Stale = False,
        overrideGlobalOptions = False,
        teardownRate = 10,
        role = "Initiator",
        pcpuLogLevel = "0",
        useMaxInitiationRate = False
)

    # If the 'override' property is set to true the specific settings for this network will override the session specific settings
    my_ixNetIxCatENodeBSimPortGroupData = Network1.getNetworkSpecificData("IxCatENodeBSimPlugin")

    my_ixNetIxCatENodeBSimPortGroupData.activities.clear()

    

    my_ixNetIxCatENodeBSimPortGroupData.associates.clear()

    

    my_ixNetIxCatENodeBSimPortGroupData.apnList.clear()

    

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetIxCatENodeBSimPortGroupData.apnList.appendItem(object = my_ixNetIxCatENodeBSimApnEntry
)

    

    my_ixNetIxCatENodeBSimPortGroupData.config(
        arp = 7,
        ipv6StaticPrefix = "B16B:00B5:DEAD:BEEF",
        s1SetupMaxOutstanding = 300,
        itemType = "IxCatENodeBSimPortGroupData",
        attach_timer_T3410 = 15,
        maxOutstandingReleases = 200,
        milenage_c1 = "00000000000000000000000000000000",
        milenage_c3 = "00000000000000000000000000000002",
        milenage_c2 = "00000000000000000000000000000001",
        adaptorLogLevel = "0",
        enableNasTracing = False,
        enableIPDefragmentation = False,
        timer_T3411 = 10,
        ddriverLogLevel = "0",
        displayLogLevel = "0",
        milenage_r4 = 64,
        milenage_r5 = 96,
        milenage_r2 = 0,
        milenage_r3 = 32,
        milenage_r1 = 64,
        autoDetectInstances = True,
        _Stale = False,
        tau_timer_T3430 = 15,
        showMessageAnalyst = False,
        qci = 4,
        s5s8InterfaceType = "7",
        pcpuLogLevel = "0",
        service_request_timer_T3417 = 5,
        instanceCount = 1,
        gbrd = 65536,
        priorityLevel = 1,
        overrideGlobalS1RateControls = False,
        bearer_resource_modify_timer_T3481 = 8,
        enableLocalPortSCTPCapture = False,
        enableGtpTeidCycle = False,
        preemptionVulnerability = True,
        preemptionCapability = True,
        gbru = 65536,
        useDefaultAPN = False,
        detach_timer_T3421 = 15,
        setupRateInitial = 100,
        s1SetupRate = 300,
        teardownRateInitial = 100,
        enableStaticIPv6Prefix = False,
        instanceIdStr = "obsolete",
        bearer_resource_alloc_timer_T3480 = 8,
        maxOutstandingRequests = 200,
        enableMilenage = False,
        suppressGtpuErrorIndication = False,
        nas_retry_count = 5,
        mbru = 65536,
        sendTeidOnAttach = True,
        milenage_c5 = "00000000000000000000000000000008",
        overrideGlobalRateControls = False,
        enableGtpuSequenceNumber = False,
        itpLogLevel = "0",
        mbrd = 65536,
        ext_service_request_timer_T3417ext = 10,
        nasRelease = "10",
        enablePerUeStats = True,
        milenage_c4 = "00000000000000000000000000000004"
)

    # If the 'override' property is set to true the specific settings for this network will override the session specific settings
    my_ixNetIPSecPortGroupData1 = Network1.getNetworkSpecificData("IPSecPlugin")

    my_ixNetIPSecPortGroupData1.activities.clear()

    

    my_ixNetIPSecPortGroupData1.associates.clear()

    

    my_ixNetIPSecPortGroupData1.config(
        useMaxPendingTunnels = False,
        itemType = "IPSecPortGroupData",
        enableESPPerStreamStats = False,
        maxInitiationRate = 50,
        enableESPReplayStats = False,
        maxPendingTunnels = 50,
        _Stale = False,
        overrideGlobalOptions = False,
        teardownRate = 10,
        role = "Initiator",
        pcpuLogLevel = "0",
        useMaxInitiationRate = False
)

    #################################################
    # Create the test controller to run the test
    #################################################
    testController = IxLoad.new("ixTestController", outputDir = True
)

    

    testController.initPythonApi()

    testController.setResultDir("RESULTS/abo_2")

    Subscriber2_Network1.setCommunityCaptureParams(Test1, True)

    Network1.portList[0].setAnalyzerPartialCapture("False;8192")


    testController.run(Test1)
    IxLoad.waitForTestFinish()

    IxLoad.waitForCaptureDataReceived()
    #################################################
    # Cleanup
    #################################################
    # Release config is only strictly necessary if enableReleaseConfigAfterRun is 0.
    testController.releaseConfig()

    IxLoad.waitForTestFinish()

    Test1.clearDUTList()

    Subscriber2_Network1.removeAllPortsFromAnalyzer()

    Traffic2_Network3.removeAllPortsFromAnalyzer()

    IxLoad.delete(chassisChain)

    IxLoad.delete(Test1)

    IxLoad.delete(profileDirectory)

    IxLoad.delete(my_ixEventHandlerSettings)

    IxLoad.delete(my_ixViewOptions)

    IxLoad.delete(Scenario1)

    IxLoad.delete(Originate)

    IxLoad.delete(Subscriber2_Network1)

    IxLoad.delete(Network1)

    IxLoad.delete(my_ixPortL1Settings)

    IxLoad.delete(Settings_3)

    IxLoad.delete(Filter_4)

    IxLoad.delete(GratARP_4)

    IxLoad.delete(TCP_3)

    IxLoad.delete(DNS_3)

    IxLoad.delete(SCTP_3)

    IxLoad.delete(Meshing_5)

    IxLoad.delete(HTTPClient1_Traffic2_HTTPServer1)

    IxLoad.delete(Ethernet_3)

    IxLoad.delete(my_ixNetDataCenterSettings)

    IxLoad.delete(my_ixNetEthernetELMPlugin)

    IxLoad.delete(my_ixNetDualPhyPlugin)

    IxLoad.delete(MAC_VLAN_9)

    IxLoad.delete(UP_IP_8)

    IxLoad.delete(eNodeB_2)

    IxLoad.delete(MAC_VLAN_11)

    IxLoad.delete(CP_IP_10)

    IxLoad.delete(User_Equipment_1)

    IxLoad.delete(my_ixNetIxCatENodeBSimNetworkActivity)

    IxLoad.delete(my_ixNetIxCatENodeBSimNetworkActivitySettings)

    IxLoad.delete(MAC_GNB)

    IxLoad.delete(IP_GNB)

    IxLoad.delete(MMEPool_R5)

    IxLoad.delete(eNB_R5)

    IxLoad.delete(my_ixNetIxCatENodeBSimResourceStatusReport)

    IxLoad.delete(my_ixNetIxCatENodeBSimLoadIndication)

    IxLoad.delete(my_ixNetIxCatENodeBSimMMEPoolEntry)

    IxLoad.delete(IP_R10_CP)

    IxLoad.delete(MAC_R9_CP)

    IxLoad.delete(VLAN_R19_CP)

    IxLoad.delete(IP_R9_UP)

    IxLoad.delete(MAC_R10_UP)

    IxLoad.delete(VLAN_R20_UP)

    IxLoad.delete(UE_R21)

    IxLoad.delete(my_ixNetIxCatENodeBSimCipheringAlgorithms)

    IxLoad.delete(my_ixNetIxCatENodeBSimUeFailureTesting)

    IxLoad.delete(my_ixNetIxCatENodeBSimUeNetworkCapabilityCIoT)

    IxLoad.delete(my_ixNetIxCatENodeBSimIntegrityAlgorithms)

    IxLoad.delete(IxCatENodeBSimUePCO_7)

    IxLoad.delete(my_ixNetIxCatENodeBSimApnEntry)

    IxLoad.delete(my_ixNetIxCatRNCIuPSQoSv1)

    IxLoad.delete(Activity_eNB_S1_MME_CP)

    IxLoad.delete(Timeline2)

    IxLoad.delete(my_ixNetIxCatENodeBSimCommandNegativeTestingNasEntry)

    IxLoad.delete(my_ixNetIxCatENodeBSimCommandNegativeTestingS1apEntry)

    IxLoad.delete(SubActivity_UE_R21)

    IxLoad.delete(Subscriber_Activity_HTTPClient1)

    IxLoad.delete(APN_1)

    IxLoad.delete(DedicatedBearer_2)

    IxLoad.delete(my_ixHttpCommand)

    IxLoad.delete(my_ixHttpHeaderString)

    IxLoad.delete(my_ixHttpHeaderString1)

    IxLoad.delete(my_ixHttpHeaderString2)

    IxLoad.delete(my_ixHttpHeaderString3)

    IxLoad.delete(DUT)

    IxLoad.delete(Terminate)

    IxLoad.delete(Traffic2_Network3)

    IxLoad.delete(Network3)

    IxLoad.delete(my_ixPortL2)

    IxLoad.delete(Settings_5)

    IxLoad.delete(Filter_5)

    IxLoad.delete(GratARP_5)

    IxLoad.delete(TCP_5)

    IxLoad.delete(DNS_5)

    IxLoad.delete(SCTP_5)

    IxLoad.delete(Meshing_4)

    IxLoad.delete(Ethernet_5)

    IxLoad.delete(my_ixNetDataCenterSettings1)

    IxLoad.delete(my_ixNetEthernetELMPlugin1)

    IxLoad.delete(my_ixNetDualPhyPlugin1)

    IxLoad.delete(MAC_VLAN_16)

    IxLoad.delete(UP_IP_15)

    IxLoad.delete(MME_3)

    IxLoad.delete(MAC_VLAN_17)

    IxLoad.delete(CP_IP_16)

    IxLoad.delete(PCRF_HSS_3)

    IxLoad.delete(MAC_VLAN_18)

    IxLoad.delete(IP_17)

    IxLoad.delete(IP_R15_CP)

    IxLoad.delete(MAC_R14_CP)

    IxLoad.delete(VLAN_R34_CP)

    IxLoad.delete(MME_R4)

    IxLoad.delete(IP_R14_UP)

    IxLoad.delete(MAC_R15_UP)

    IxLoad.delete(VLAN_R35_UP)

    IxLoad.delete(PCRF_R3)

    IxLoad.delete(my_ixNetIxCatServerQoSv1)

    IxLoad.delete(Bearer_R3)

    IxLoad.delete(UE_R23)

    IxLoad.delete(my_ixNetIxCatServerUeApnEntryBase)

    IxLoad.delete(Activity_HTTPServer1)

    IxLoad.delete(_Match_Longest_)

    IxLoad.delete(my_PageObject)

    IxLoad.delete(_200_OK)

    IxLoad.delete(my_PageObject1)

    IxLoad.delete(my_PageObject2)

    IxLoad.delete(my_PageObject3)

    IxLoad.delete(my_PageObject4)

    IxLoad.delete(my_PageObject5)

    IxLoad.delete(my_PageObject6)

    IxLoad.delete(my_PageObject7)

    IxLoad.delete(my_PageObject8)

    IxLoad.delete(my_PageObject9)

    IxLoad.delete(UserCookie)

    IxLoad.delete(firstName)

    IxLoad.delete(lastName)

    IxLoad.delete(LoginCookie)

    IxLoad.delete(name)

    IxLoad.delete(password)

    IxLoad.delete(AsciiCustomPayload)

    IxLoad.delete(HexCustomPayload)

    IxLoad.delete(_201)

    IxLoad.delete(_404_PageNotFound)

    IxLoad.delete(destination)

    IxLoad.delete(my_ixNetMacSessionData)

    IxLoad.delete(my_ixNetIpSessionData)

    IxLoad.delete(my_ixNetIxCatENodeBSimPluginSessionData)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci2TosEntry)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci3)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci4)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci5)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci6)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci7)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci8)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci9)

    IxLoad.delete(my_ixNetIxCatENodeBSimQci10)

    IxLoad.delete(my_ixNetIPSecSessionData)

    IxLoad.delete(my_ixNetIPSecCertificates)

    IxLoad.delete(my_ixNetIPSecCertManager)

    IxLoad.delete(my_ixNetIPSecTunnelSetup)

    IxLoad.delete(my_ixNetIxCatMMEPluginSessionData)

    IxLoad.delete(my_ixNetIxCatMMEQci2TosEntry)

    IxLoad.delete(my_ixNetIxCatMMEQci3)

    IxLoad.delete(my_ixNetIxCatMMEQci4)

    IxLoad.delete(my_ixNetIxCatMMEQci5)

    IxLoad.delete(my_ixNetIxCatMMEQci6)

    IxLoad.delete(my_ixNetIxCatMMEQci7)

    IxLoad.delete(my_ixNetIxCatMMEQci8)

    IxLoad.delete(my_ixNetIxCatMMEQci9)

    IxLoad.delete(my_ixNetIxCatMMEQci10)

    IxLoad.delete(my_ixNetIxCatMMEPortGroupData)

    IxLoad.delete(my_ixNetIPSecPortGroupData)

    IxLoad.delete(my_ixNetIxCatENodeBSimPortGroupData)

    IxLoad.delete(my_ixNetIPSecPortGroupData1)

    IxLoad.delete(testController)



    #################################################
    # Disconnect / Release application lock
    #################################################
except Exception, e:
    print str(e)

IxLoad.delete(logEngine)
IxLoad.delete(logger)

IxLoad.disconnect()
