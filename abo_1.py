    #################################################
    # IxLoad ScriptGen created script
    # Test1 serialized using version 8.50.115.124
    # abo_1.py made on 4 18 2019 17:16
    #################################################
    


from IxLoad import IxLoad

IxLoad = IxLoad()

IxLoad.connect("1.2.3.4")


try:

    logtag = "IxLoad-api"
    logName = "abo_1"
    logger = IxLoad.new("ixLogger", logtag, 1)
    logEngine = logger.getEngine()
    logEngine.setLevels(IxLoad.ixLogger.kLevelDebug, IxLoad.ixLogger.kLevelInfo)
    logEngine.setFile(logName, 5, 256, 1)

    IxLoad.loadAppPlugin("FTP")
    IxLoad.loadAppPlugin("HTTP")

    #################################################
    # Build chassis chain
    #################################################
    chassisChain = IxLoad.new("ixChassisChain")

    chassisChain.addChassis("172.30.227.250")

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

    TrafficFlow1 = scenarioFactory.create("Scenario")

    TrafficFlow1.columnList.clear()

    Originate = IxLoad.new("ixTrafficColumn")

    Originate.elementList.clear()

    #################################################
    # Create ScenarioElement kSubscriberNetTraffic
    #################################################
    Subscriber1_Network1_1 = scenarioElementFactory.create(IxLoad.ixScenarioElementType.kSubscriberNetTraffic)

    

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
    # Network Network1_1 of NetTraffic Subscriber1@Network1_1
    #################################################
    Network1_1 = Subscriber1_Network1_1.cget("network")

    Network1_1.portList.appendItem(
        chassisId = 1,
        cardId = 5,
        portId = 1
)

    Network1_1.portList[0].setPortCaptureEnable(True)

    Network1_1.portList[0].setPortCaptureFileName("RESULTS\\\\abo_1\\\\Port_1_5_1_capture.cap")

    Network1_1.globalPlugins.clear()

    

    Settings_6 = IxLoad.new("ixNetIxLoadSettingsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1_1.globalPlugins.appendItem(object = Settings_6
)

    

    Settings_6.config(
        teardownInterfaceWithUser = False,
        _Stale = False,
        itemType = "IxLoadSettingsPlugin",
        interfaceBehavior = 1
)

    Filter_7 = IxLoad.new("ixNetFilterPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1_1.globalPlugins.appendItem(object = Filter_7
)

    

    Filter_7.config(
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

    GratARP_7 = IxLoad.new("ixNetGratArpPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1_1.globalPlugins.appendItem(object = GratARP_7
)

    

    GratARP_7.config(
        itemType = "GratArpPlugin",
        forwardGratArp = False,
        enabled = True,
        maxFramesPerSecond = 0,
        _Stale = False,
        rateControlEnabled = False
)

    TCP_6 = IxLoad.new("ixNetTCPPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1_1.globalPlugins.appendItem(object = TCP_6
)

    

    TCP_6.config(
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

    DNS_6 = IxLoad.new("ixNetDnsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1_1.globalPlugins.appendItem(object = DNS_6
)

    

    DNS_6.hostList.clear()

    

    DNS_6.searchList.clear()

    

    DNS_6.nameServerList.clear()

    

    DNS_6.config(
        domain = "",
        _Stale = False,
        itemType = "DnsPlugin",
        timeout = 30
)

    SCTP_2 = IxLoad.new("ixNetSctpPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network1_1.globalPlugins.appendItem(object = SCTP_2
)

    

    SCTP_2.config(
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
    Network1_1.globalPlugins.appendItem(object = Meshing_5
)

    

    Meshing_5.trafficMaps.clear()

    

    Meshing_5.config(
        _Stale = False,
        itemType = "MeshingPlugin"
)

    Network1_1.config(
        comment = "",
        name = "Network1_1",
        lineSpeed = "Default",
        aggregation = 0,
        portL1Settings = my_ixPortL1Settings
)

    Ethernet_6 = Network1_1.getL1Plugin()

    

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

    Ethernet_6.childrenList.clear()

    

    MAC_VLAN_13 = IxLoad.new("ixNetL2EthernetPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Ethernet_6.childrenList.appendItem(object = MAC_VLAN_13
)

    

    MAC_VLAN_13.childrenList.clear()

    

    UP_IP_10 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_13.childrenList.appendItem(object = UP_IP_10
)

    

    UP_IP_10.childrenList.clear()

    

    eNodeB_2 = IxLoad.new("ixNetIxCatENodeBSimPlugin")

    # ixNet objects need to be added in the list before they are configured!
    UP_IP_10.childrenList.appendItem(object = eNodeB_2
)

    

    MAC_VLAN_16 = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_VLAN_16.childrenList.clear()

    

    IP_12 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_16.childrenList.appendItem(object = IP_12
)

    

    IP_12.childrenList.clear()

    

    IP_12.extensionList.clear()

    

    IP_12.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_16.extensionList.clear()

    

    MAC_VLAN_16.config(
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
        macPluginForCP = MAC_VLAN_16,
        uePlugin = User_Equipment_1,
        networkActivity = my_ixNetIxCatENodeBSimNetworkActivity,
        macPluginForGNB = MAC_GNB
)

    UP_IP_10.extensionList.clear()

    

    UP_IP_10.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_13.extensionList.clear()

    

    MAC_VLAN_13.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    Ethernet_6.extensionList.clear()

    

    Ethernet_6.config(
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

    MMEPool_R2 = IxLoad.new("ixNetIxCatENodeBSimMMERange")

    # ixNet objects need to be added in the list before they are configured.
    eNodeB_2.mmeRangeList.appendItem(object = MMEPool_R2
)

    

    MMEPool_R2.config(
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

    eNB_R2 = IxLoad.new("ixNetIxCatENodeBSimRange")

    # ixNet objects need to be added in the list before they are configured.
    eNodeB_2.enodebRangeList.appendItem(object = eNB_R2
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

    eNB_R2.x2eNodeBList.clear()

    

    eNB_R2.mhList.clear()

    

    eNB_R2.mmePoolList.clear()

    

    my_ixNetIxCatENodeBSimMMEPoolEntry = IxLoad.new("ixNetIxCatENodeBSimMMEPoolEntry")

    # ixNet objects need to be added in the list before they are configured!
    eNB_R2.mmePoolList.appendItem(object = my_ixNetIxCatENodeBSimMMEPoolEntry
)

    

    my_ixNetIxCatENodeBSimMMEPoolEntry.config(
        _Stale = False,
        itemType = "IxCatENodeBSimMMEPoolEntry",
        nextMMEPool = MMEPool_R2
)

    eNB_R2.config(
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

    IP_R9 = eNB_R2.getLowerRelatedRangeByIndex("IpV4V6Range", 0)

    IP_R9.config(
        count = 1,
        enableGatewayArp = False,
        randomizeSeed = 1052501568,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = False,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "0.0.0.1",
        prefix = 24,
        _Stale = False,
        gatewayIncrement = "0.0.0.0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "4.11.5.1",
        ipAddress = "4.11.5.20",
        ipType = "IPv4"
)

    MAC_R9 = IP_R9.getLowerRelatedRange("MacRange")

    MAC_R9.config(
        count = 1,
        itemType = "MacRange",
        enabled = False,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:0B:05:14:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R12 = IP_R9.getLowerRelatedRange("VlanIdRange")

    VLAN_R12.config(
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

    IP_R8 = eNB_R2.getLowerRelatedRangeByIndex("IpV4V6Range", 1)

    IP_R8.config(
        count = 1,
        enableGatewayArp = False,
        randomizeSeed = 1465824867,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = True,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "0.0.0.1",
        prefix = 22,
        _Stale = False,
        gatewayIncrement = "0.0.0.0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "4.23.0.1",
        ipAddress = "4.23.0.2",
        ipType = "IPv4"
)

    MAC_R8 = IP_R8.getLowerRelatedRange("MacRange")

    MAC_R8.config(
        count = 1,
        itemType = "MacRange",
        enabled = True,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:17:00:02:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R11 = IP_R8.getLowerRelatedRange("VlanIdRange")

    VLAN_R11.config(
        incrementStep = 1,
        innerIncrement = 1,
        uniqueCount = 1,
        itemType = "VlanIdRange",
        tpid = "0x8100",
        idIncrMode = 2,
        enabled = True,
        innerFirstId = 1,
        increment = 0,
        priority = 1,
        _Stale = False,
        firstId = 30,
        innerTpid = "0x8100",
        innerIncrementStep = 1,
        innerUniqueCount = 4094,
        innerEnable = False,
        innerPriority = 1
)

    eNodeB_2.enodebUeRangeList.clear()

    UE_R3 = IxLoad.new("ixNetIxCatENodeBSimUeRange")

    # ixNet objects need to be added in the list before they are configured.
    eNodeB_2.enodebUeRangeList.appendItem(object = UE_R3
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

    UE_R3.pcoList.clear()

    

    IxCatENodeBSimUePCO_3 = IxLoad.new("ixNetIxCatENodeBSimUePCO")

    # ixNet objects need to be added in the list before they are configured!
    UE_R3.pcoList.appendItem(object = IxCatENodeBSimUePCO_3
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
        pcoProtocol = "Custom",
        mbrd = 0,
        emergencyApn = False,
        qosv1 = my_ixNetIxCatRNCIuPSQoSv1
)

    IxCatENodeBSimUePCO_3.config(
        authUserIdIncr = False,
        itemType = "IxCatENodeBSimUePCO",
        authCustomPCO = "8080",
        authPasswordIncr = False,
        enabled = True,
        _Stale = False,
        authUserId = "user",
        authPassword = "password",
        apnEntry = my_ixNetIxCatENodeBSimApnEntry
)

    UE_R3.mobilityPathList.clear()

    

    UE_R3.config(
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
        parentRange = eNB_R2,
        ueNetworkCapability = my_ixNetIxCatENodeBSimUeNetworkCapabilityCIoT,
        integrityAlgorithm = my_ixNetIxCatENodeBSimIntegrityAlgorithms
)

    eNodeB_2.enbAssociationList.clear()

    

    #################################################
    # Creating the IP Distribution Groups
    #################################################
    Subscriber1_Network1_1.config(
        enable = True,
        tcpAccelerationAllowedFlag = True,
        network = Network1_1
)

    #################################################
    # Network Activities for Subscriber1@Network1_1
    #################################################
    Activity_eNB_S1_MME_CP = Subscriber1_Network1_1.networkActivityList.getNetworkActivityByPluginType(eNodeB_2, "Control Plane")

    #################################################
    # Timeline3 for activities HTTPClient1, eNB S1-MME CP
    #################################################
    Timeline3 = IxLoad.new("ixTimeline")

    Timeline3.config(
        rampUpValue = 1,
        offlineTime = 0,
        rampDownTime = 20,
        standbyTime = 0,
        rampDownValue = 0,
        iterations = 1,
        rampUpInterval = 1,
        sustainTime = 20,
        timelineType = 0,
        name = "Timeline3"
)

    Activity_eNB_S1_MME_CP.config(
        enable = True,
        timeline = Timeline3
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
        value = "178a7f32dd070741120bf654f060810103d890f31805f0f0000010002c0201d03127268080211001000010810600000000830600000000000c00000100000d00000300000a00001000c05254f06021fb5c1004901103575882f15d0103e0c1",
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
        value = "006440080022f60101389010004340060022f6011011",
        _Stale = False,
        messageType = 20,
        ieNo = 5
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
        minimumInterval = 1000,
        maximumInterval = 1000,
        cmdName = "Think 4"
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

    Activity_eNB_S1_MME_CP.agent.pm.commands.appendItem(
        commandType = "THINK",
        minimumInterval = 1000,
        maximumInterval = 1000,
        cmdName = "Think 3"
)

    Activity_eNB_S1_MME_CP.setPrimaryObjectiveType("None")

    # Sub-activities are automatically added for each associated endpoint range
    Activity_eNB_S1_MME_CP_numSubActivities = Activity_eNB_S1_MME_CP.subActivities.indexCount()

    #################################################
    # Network Sub-activity for Range UE-R3
    #################################################
    SubActivity_UE_R3 = Activity_eNB_S1_MME_CP.subActivities.getItem(0)

    #################################################
    # Subscriber Activity HTTPClient1 of NetTraffic Subscriber1@Network1_1
    #################################################
    Subscriber_Activity_HTTPClient1 = Subscriber1_Network1_1.activityList.appendItem(protocolAndType = "HTTP Client"
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
        timeline = Timeline3
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

    

    my_ixThinkCommand = IxLoad.new("ixThinkCommand")

    my_ixThinkCommand.config(
        commandType = "THINK",
        minimumInterval = 1000,
        maximumInterval = 1000,
        cmdName = "Think 2"
)

    Subscriber_Activity_HTTPClient1.agent.actionList.appendItem(object = my_ixThinkCommand
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

    Subscriber1_Network1_1.traffic.config(name = "Subscriber1"
)

    Subscriber1_Network1_1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeThroughputAcceleration, False)

    Subscriber1_Network1_1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeFCoEOffload, True)

    Subscriber1_Network1_1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeBPS, True)

    Subscriber1_Network1_1.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeL23, True)

    Subscriber1_Network1_1.setTcpAccelerationAllowed(IxLoad.ixAgent.kTcpAcceleration, True)

    Subscriber1_Network1_1.setShowActualCPUUtilizationModeAllowed(False)

    Originate.elementList.appendItem(object = Subscriber1_Network1_1
)

    

    Originate.config(name = "Originate"
)

    TrafficFlow1.columnList.appendItem(object = Originate
)

    

    DUT = IxLoad.new("ixTrafficColumn")

    DUT.elementList.clear()

    DUT.config(name = "DUT"
)

    TrafficFlow1.columnList.appendItem(object = DUT
)

    

    Terminate = IxLoad.new("ixTrafficColumn")

    Terminate.elementList.clear()

    #################################################
    # Create ScenarioElement kNetTraffic
    #################################################
    Traffic4_Network2 = scenarioElementFactory.create(IxLoad.ixScenarioElementType.kNetTraffic)

    

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
    # Network Network2 of NetTraffic Traffic4@Network2
    #################################################
    Network2 = Traffic4_Network2.cget("network")

    Network2.portList.appendItem(
        chassisId = 1,
        cardId = 9,
        portId = 1
)

    Network2.globalPlugins.clear()

    

    Settings_4 = IxLoad.new("ixNetIxLoadSettingsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network2.globalPlugins.appendItem(object = Settings_4
)

    

    Settings_4.config(
        teardownInterfaceWithUser = False,
        _Stale = False,
        itemType = "IxLoadSettingsPlugin",
        interfaceBehavior = 0
)

    Filter_5 = IxLoad.new("ixNetFilterPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network2.globalPlugins.appendItem(object = Filter_5
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
    Network2.globalPlugins.appendItem(object = GratARP_5
)

    

    GratARP_5.config(
        itemType = "GratArpPlugin",
        forwardGratArp = False,
        enabled = True,
        maxFramesPerSecond = 0,
        _Stale = False,
        rateControlEnabled = False
)

    TCP_4 = IxLoad.new("ixNetTCPPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network2.globalPlugins.appendItem(object = TCP_4
)

    

    TCP_4.config(
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

    DNS_4 = IxLoad.new("ixNetDnsPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network2.globalPlugins.appendItem(object = DNS_4
)

    

    DNS_4.hostList.clear()

    

    DNS_4.searchList.clear()

    

    DNS_4.nameServerList.clear()

    

    DNS_4.config(
        domain = "",
        _Stale = False,
        itemType = "DnsPlugin",
        timeout = 30
)

    Meshing_3 = IxLoad.new("ixNetMeshingPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Network2.globalPlugins.appendItem(object = Meshing_3
)

    

    Meshing_3.trafficMaps.clear()

    

    Meshing_3.config(
        _Stale = False,
        itemType = "MeshingPlugin"
)

    Network2.config(
        comment = "",
        name = "Network2",
        lineSpeed = "Default",
        aggregation = 0,
        portL1Settings = my_ixPortL2
)

    Ethernet_4 = Network2.getL1Plugin()

    

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

    Ethernet_4.childrenList.clear()

    

    MAC_VLAN_5 = IxLoad.new("ixNetL2EthernetPlugin")

    # ixNet objects need to be added in the list before they are configured!
    Ethernet_4.childrenList.appendItem(object = MAC_VLAN_5
)

    

    MAC_VLAN_5.childrenList.clear()

    

    DualStackIP_1 = IxLoad.new("ixNetDualStackIPPlugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_5.childrenList.appendItem(object = DualStackIP_1
)

    

    DualStackIP_1.childrenList.clear()

    

    SGW_S11_S1_U_1 = IxLoad.new("ixNetEGTPPlugin_SGW")

    # ixNet objects need to be added in the list before they are configured!
    DualStackIP_1.childrenList.appendItem(object = SGW_S11_S1_U_1
)

    

    MAC_VLAN_11 = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_VLAN_11.childrenList.clear()

    

    UP_IP_9 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_11.childrenList.appendItem(object = UP_IP_9
)

    

    UP_IP_9.childrenList.clear()

    

    UP_IP_9.extensionList.clear()

    

    UP_IP_9.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_11.extensionList.clear()

    

    MAC_VLAN_11.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    MAC_VLAN_10 = IxLoad.new("ixNetL2EthernetPlugin")

    MAC_VLAN_10.childrenList.clear()

    

    CP_IP_8 = IxLoad.new("ixNetIpV4V6Plugin")

    # ixNet objects need to be added in the list before they are configured!
    MAC_VLAN_10.childrenList.appendItem(object = CP_IP_8
)

    

    CP_IP_8.childrenList.clear()

    

    CP_IP_8.extensionList.clear()

    

    CP_IP_8.config(
        _Stale = False,
        itemType = "IpV4V6Plugin"
)

    MAC_VLAN_10.extensionList.clear()

    

    MAC_VLAN_10.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    my_ixNetEGTPNetworkActivitySettings_SGW = IxLoad.new("ixNetEGTPNetworkActivitySettings_SGW")

    my_ixNetEGTPNetworkActivitySettings_SGW.config(
        implicitSynchronization = True,
        _Stale = False,
        itemType = "EGTPNetworkActivitySettings_SGW"
)

    my_ixNetEGTPNetworkActivity_SGW = IxLoad.new("ixNetEGTPNetworkActivity_SGW")

    my_ixNetEGTPNetworkActivity_SGW.config(
        _Stale = False,
        itemType = "EGTPNetworkActivity_SGW",
        activitySettings = my_ixNetEGTPNetworkActivitySettings_SGW
)

    SGW_S11_S1_U_1.childrenList.clear()

    

    SGW_S11_S1_U_1.extensionList.clear()

    

    SGW_S11_S1_U_1.config(
        _Stale = False,
        itemType = "EGTPPlugin_SGW",
        macPluginForUP = MAC_VLAN_11,
        macPluginForCP = MAC_VLAN_10,
        networkActivity = my_ixNetEGTPNetworkActivity_SGW
)

    DualStackIP_1.rangeGroups.clear()

    

    DualStackIP_1.extensionList.clear()

    

    DualStackIP_1.config(
        _Stale = False,
        itemType = "DualStackIPPlugin"
)

    MAC_VLAN_5.extensionList.clear()

    

    MAC_VLAN_5.config(
        _Stale = False,
        itemType = "L2EthernetPlugin"
)

    Ethernet_4.extensionList.clear()

    

    Ethernet_4.config(
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
    SGW_S11_S1_U_1.sgwRangeList.clear()

    SGW_R1 = IxLoad.new("ixNetEGTPSgwRange_S11SGW")

    # ixNet objects need to be added in the list before they are configured.
    SGW_S11_S1_U_1.sgwRangeList.appendItem(object = SGW_R1
)

    

    SGW_R1.changeReportingList.clear()

    

    SGW_R1.config(
        t3UpdateBearerReq = 3,
        userPlaneEchoRequestT3 = 3,
        itemType = "EGTPSgwRange_S11SGW",
        n3EchoReq = 5,
        restartSeed = 1,
        publishStats = False,
        controlPlaneLBType = "2",
        userPlaneEchoRequestN3 = 5,
        t3PGWRestartNotification = 3,
        userPlaneEchoInterval = 60,
        useCpIp = False,
        restartValue = 0,
        enableDDN = False,
        enablePRN = False,
        dDNPercentage = 50,
        n3UpdateBearerReq = 5,
        n3CreateBearerReq = 5,
        pRNTimeout = 20,
        changeReportingMode = 0,
        t3DeleteBearerReq = 3,
        enableEchoRequest = False,
        _Stale = False,
        enableDDNPercentage = False,
        t3MMEHandoverInProgress = 3,
        t3DownlinkDataNotification = 3,
        useUpIp = False,
        n3DownlinkDataNotification = 5,
        t3CreateBearerReq = 3,
        n3DeleteBearerReq = 5,
        t3EchoReq = 3,
        n3PGWRestartNotification = 5,
        enabled = True,
        dDNTimeout = 20,
        n3MMEHandoverInProgress = 5,
        restartCounter = 0,
        enableUserPlaneEchoRequest = False
)

    IP_R11 = SGW_R1.getLowerRelatedRangeByIndex("IpV4V6Range", 0)

    IP_R11.config(
        count = 100,
        enableGatewayArp = False,
        randomizeSeed = 3176251208,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = False,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "0.0.0.1",
        prefix = 24,
        _Stale = False,
        gatewayIncrement = "0.0.0.0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "0.0.0.0",
        ipAddress = "4.11.5.211",
        ipType = "IPv4"
)

    MAC_R10 = IP_R11.getLowerRelatedRange("MacRange")

    MAC_R10.config(
        count = 100,
        itemType = "MacRange",
        enabled = False,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:0B:05:D3:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R18 = IP_R11.getLowerRelatedRange("VlanIdRange")

    VLAN_R18.config(
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

    IP_R12 = SGW_R1.getLowerRelatedRangeByIndex("IpV4V6Range", 1)

    IP_R12.config(
        count = 100,
        enableGatewayArp = False,
        randomizeSeed = 1951173227,
        mss = 1460,
        itemType = "IpV4V6Range",
        autoIpTypeEnabled = False,
        autoCountEnabled = False,
        enabled = False,
        autoMacGeneration = True,
        publishStats = False,
        incrementBy = "0.0.0.1",
        prefix = 24,
        _Stale = False,
        gatewayIncrement = "0.0.0.0",
        gatewayIncrementMode = "perSubnet",
        generateStatistics = False,
        randomizeAddress = False,
        gatewayAddress = "0.0.0.0",
        ipAddress = "4.11.6.55",
        ipType = "IPv4"
)

    MAC_R11 = IP_R12.getLowerRelatedRange("MacRange")

    MAC_R11.config(
        count = 100,
        itemType = "MacRange",
        enabled = False,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:0B:06:37:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R19 = IP_R12.getLowerRelatedRange("VlanIdRange")

    VLAN_R19.config(
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

    IP_R10 = SGW_R1.getLowerRelatedRange("DualStackIPRange")

    IP_R10.config(
        prefixV6 = 112,
        prefixV4 = 22,
        itemType = "DualStackIPRange",
        autoCountEnabled = False,
        autoMacGeneration = True,
        publishStats = False,
        incrementByV6 = "0::1",
        incrementByV4 = "0.0.0.1",
        gatewayAddressV4 = "4.23.0.1",
        gatewayAddressV6 = "0::0",
        mss = 1460,
        randomizeAddress = False,
        _Stale = False,
        generateStatistics = False,
        enableGatewayArp = False,
        gatewayIncrementV4 = "0.0.0.0",
        gatewayIncrementV6 = "0::0",
        ipAddressV4 = "4.23.0.230",
        ipType = "IPv4",
        count = 1,
        ipAddressV6 = "::A0A:1",
        enabled = True,
        gatewayIncrementModeV4 = "perSubnet",
        gatewayIncrementModeV6 = "perSubnet",
        randomizeSeed = 3816516514
)

    MAC_R12 = IP_R10.getLowerRelatedRange("MacRange")

    MAC_R12.config(
        count = 1,
        itemType = "MacRange",
        enabled = True,
        incrementBy = "00:00:00:00:00:01",
        mac = "00:04:17:00:E6:00",
        _Stale = False,
        mtu = 1500
)

    VLAN_R17 = IP_R10.getLowerRelatedRange("VlanIdRange")

    VLAN_R17.config(
        incrementStep = 1,
        innerIncrement = 1,
        uniqueCount = 1,
        itemType = "VlanIdRange",
        tpid = "0x8100",
        idIncrMode = 2,
        enabled = True,
        innerFirstId = 1,
        increment = 0,
        priority = 1,
        _Stale = False,
        firstId = 30,
        innerTpid = "0x8100",
        innerIncrementStep = 1,
        innerUniqueCount = 4094,
        innerEnable = False,
        innerPriority = 1
)

    SGW_S11_S1_U_1.rangeList.clear()

    PCRF_R1 = IxLoad.new("ixNetEGTPRange_SGW")

    # ixNet objects need to be added in the list before they are configured.
    SGW_S11_S1_U_1.rangeList.appendItem(object = PCRF_R1
)

    

    my_ixNetGTPNGQoSv1 = IxLoad.new("ixNetGTPNGQoSv1")

    my_ixNetGTPNGQoSv1.config(
        reliabilityClass = 2,
        itemType = "GTPNGQoSv1",
        sduErrorRatio = 6,
        maxBitRateDLEx = 0,
        allocationRetentionPriority = 2,
        guaranteedBitRateUL = 64,
        maxSDUSize = 151,
        sourceStatisticsDescriptor = 0,
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
        meanThroughput = 31,
        maxBitRateUL = 8640,
        transferDelay = 4000,
        trafficClass = 4,
        deliveryOfErroneousSDU = 1,
        guaranteedBitRateDLEx = 0,
        residualBER = 7
)

    PCRF_R1.bearerList.clear()

    

    PCRF_R1.config(
        apn_AMBRU = 8640,
        userPlaneIpCount = 1,
        itemType = "EGTPRange_SGW",
        enableDefaultBearerTft = False,
        sendDNSServerIp = False,
        publishStats = False,
        apn_AMBRD = 8640,
        db_qci = 9,
        pcscfIpType = "IPv4",
        acceptIncAPN = False,
        pcscfIpv4 = "0.0.0.0",
        defaultBearerLifetimeTimer = 10,
        pcscfIpv6 = "1::1",
        db_pvi = False,
        enableDefaultBearerLifetime = False,
        db_pl = 1,
        apn = "ixiaint.lguplus.co.kr.mnc006.mcc450.gprs",
        updateDefaultBearerTft = False,
        mss = 1424,
        poolSize = 100,
        _Stale = False,
        poolStartIPv4 = "172.16.0.1",
        enableBCMUpdate = False,
        poolStartIp = "",
        poolStartIPv6 = "::AC10:65",
        userPlaneIPv6Address = "::1616:1616",
        nidbCreationDelay = 1,
        userPlaneIPv4Address = "22.22.22.22",
        poolIncrementByIPv6 = "::1",
        totalCount = 1,
        defaultBearerTft = "3000035013C4",
        requireAuthentication = False,
        ims_apn = False,
        enableNIDBCreationDelay = False,
        iMSI = "450061015000000",
        ipType = "IPv4",
        poolIncrementByIPv4 = "0.0.0.1",
        pcoDns = 2,
        fragmentation = False,
        db_pci = False,
        db_gbrd = 8640,
        db_mbrd = 8640,
        enabled = True,
        mac = "AA:BB:CC:00:00:01",
        roundRobinDistribution = False,
        isEmergencyApn = False,
        db_gbru = 8640,
        db_mbru = 8640,
        bcmUpdateDelay = 60,
        pcscfIpv6Secondary = "1::2",
        userPlaneIpAddress = "",
        qosv1 = my_ixNetGTPNGQoSv1
)

    #################################################
    # Creating the IP Distribution Groups
    #################################################
    Traffic4_Network2.config(
        enable = 1,
        tcpAccelerationAllowedFlag = True,
        network = Network2
)

    #################################################
    # Network Activities for Traffic4@Network2
    #################################################
    Activity_eGTP_Control_Plane = Traffic4_Network2.networkActivityList.getNetworkActivityByPluginType(SGW_S11_S1_U_1, "Control Plane")

    _Match_Longest_ = IxLoad.new("ixMatchLongestTimeline")

    

    Activity_eGTP_Control_Plane.config(
        enable = True,
        timeline = _Match_Longest_
)

    Activity_eGTP_Control_Plane.agent.config(
        cmdListLoops = 0,
        flowPercentage = 100.0
)

    Activity_eGTP_Control_Plane.agent.pm.commands.clear()

    Activity_eGTP_Control_Plane.setPrimaryObjectiveType("None")

    #################################################
    # Activity FTPServer1 of NetTraffic Traffic4@Network2
    #################################################
    Activity_FTPServer1 = Traffic4_Network2.activityList.appendItem(protocolAndType = "FTP Server"
)

    _Match_Longest_1 = IxLoad.new("ixMatchLongestTimeline")

    

    Activity_FTPServer1.config(
        enable = True,
        name = "FTPServer1",
        timeline = _Match_Longest_1
)

    Activity_FTPServer1.agent.realFileList.clear()

    my_RealFileObject = IxLoad.new("RealFileObject")

    my_RealFileObject.config(
        payloadFile = "<Dummy File>",
        page = "/#1"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject
)

    

    my_RealFileObject1 = IxLoad.new("RealFileObject")

    my_RealFileObject1.config(
        payloadFile = "<Dummy File>",
        page = "/#4"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject1
)

    

    my_RealFileObject2 = IxLoad.new("RealFileObject")

    my_RealFileObject2.config(
        payloadFile = "<Dummy File>",
        page = "/#16"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject2
)

    

    my_RealFileObject3 = IxLoad.new("RealFileObject")

    my_RealFileObject3.config(
        payloadFile = "<Dummy File>",
        page = "/#64"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject3
)

    

    my_RealFileObject4 = IxLoad.new("RealFileObject")

    my_RealFileObject4.config(
        payloadFile = "<Dummy File>",
        page = "/#256"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject4
)

    

    my_RealFileObject5 = IxLoad.new("RealFileObject")

    my_RealFileObject5.config(
        payloadFile = "<Dummy File>",
        page = "/#1024"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject5
)

    

    my_RealFileObject6 = IxLoad.new("RealFileObject")

    my_RealFileObject6.config(
        payloadFile = "<Dummy File>",
        page = "/#4096"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject6
)

    

    my_RealFileObject7 = IxLoad.new("RealFileObject")

    my_RealFileObject7.config(
        payloadFile = "<Dummy File>",
        page = "/#16384"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject7
)

    

    my_RealFileObject8 = IxLoad.new("RealFileObject")

    my_RealFileObject8.config(
        payloadFile = "<Dummy File>",
        page = "/#65536"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject8
)

    

    my_RealFileObject9 = IxLoad.new("RealFileObject")

    my_RealFileObject9.config(
        payloadFile = "<Dummy File>",
        page = "/#262144"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject9
)

    

    my_RealFileObject10 = IxLoad.new("RealFileObject")

    my_RealFileObject10.config(
        payloadFile = "<Dummy File>",
        page = "/#1048576"
)

    Activity_FTPServer1.agent.realFileList.appendItem(object = my_RealFileObject10
)

    

    Activity_FTPServer1.agent.config(
        enableTos = 0,
        cmdListLoops = 0,
        enableEsm = 0,
        reliabilityTOS = 0,
        flowPercentage = 100.0,
        vlanPriority = 0,
        tos = 0,
        ftpPort = "21",
        delayTOS = 0,
        precedenceTOS = 0,
        throughputTOS = 0,
        esm = 1460,
        enableVlanPriority = 0
)

    Traffic4_Network2.traffic.config(name = "Traffic4"
)

    Traffic4_Network2.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeThroughputAcceleration, False)

    Traffic4_Network2.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeFCoEOffload, True)

    Traffic4_Network2.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeBPS, True)

    Traffic4_Network2.setPortOperationModeAllowed(IxLoad.ixPort.kOperationModeL23, True)

    Traffic4_Network2.setTcpAccelerationAllowed(IxLoad.ixAgent.kTcpAcceleration, True)

    Traffic4_Network2.setShowActualCPUUtilizationModeAllowed(False)

    Terminate.elementList.appendItem(object = Traffic4_Network2
)

    

    Terminate.config(name = "Terminate"
)

    TrafficFlow1.columnList.appendItem(object = Terminate
)

    

    TrafficFlow1.appMixList.clear()

    TrafficFlow1.links.clear()

    TrafficFlow1.config(name = "TrafficFlow1"
)

    Test1.config(
        comment = "",
        networkFailureThreshold = 0,
        statViewThroughputUnits = "Kbps",
        showNetworkDiagnosticsAfterRunStops = True,
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
        csvInterval = 2,
        name = "Test1",
        downgradeAppLibFlowsToLatestValidVersion = True,
        statsRequired = True,
        isFrameSizeDistributionViewSupported = False,
        enableForceOwnership = True,
        enableNetworkDiagnostics = True,
        allowMixedObjectiveTypes = False,
        currentUniqueIDForAgent = 15,
        profileDirectory = profileDirectory,
        eventHandlerSettings = my_ixEventHandlerSettings,
        captureViewOptions = my_ixViewOptions
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

    my_ixNetEGTPPluginSessionData_SGW = Test1.getSessionSpecificData("EGTPPlugin_SGW")

    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.clear()

    

    my_ixNetEGTPQci2TosEntry_SGW = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci2TosEntry_SGW
)

    

    my_ixNetEGTPQci2TosEntry_SGW.config(
        tos = "10",
        qci = 1,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci3 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci3
)

    

    my_ixNetEGTPQci3.config(
        tos = "10",
        qci = 2,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci4 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci4
)

    

    my_ixNetEGTPQci4.config(
        tos = "10",
        qci = 3,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci5 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci5
)

    

    my_ixNetEGTPQci5.config(
        tos = "10",
        qci = 4,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci6 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci6
)

    

    my_ixNetEGTPQci6.config(
        tos = "10",
        qci = 5,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci7 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci7
)

    

    my_ixNetEGTPQci7.config(
        tos = "10",
        qci = 6,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci8 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci8
)

    

    my_ixNetEGTPQci8.config(
        tos = "10",
        qci = 7,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci9 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci9
)

    

    my_ixNetEGTPQci9.config(
        tos = "10",
        qci = 8,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPQci10 = IxLoad.new("ixNetEGTPQci2TosEntry_SGW")

    # ixNet objects need to be added in the list before they are configured!
    my_ixNetEGTPPluginSessionData_SGW.qci2TosMap.appendItem(object = my_ixNetEGTPQci10
)

    

    my_ixNetEGTPQci10.config(
        tos = "10",
        qci = 9,
        enable = True,
        _Stale = False,
        itemType = "EGTPQci2TosEntry_SGW"
)

    my_ixNetEGTPPluginSessionData_SGW.config(
        enableGatewayArp = False,
        maxOutstandingRequests = 300,
        itemType = "EGTPPluginSessionData_SGW",
        useMaxRatesForDcp = True,
        ignoreUnresolvedIPs = False,
        individualARPTimeOut = 500,
        maxMbrUAndD = 1099511627775,
        tsSpec = "R10_DECEMBER2011_SPEC",
        enableDynamicQosCtrl = False,
        maxOutstandingReleases = 300,
        maxOutstandingGatewayArpRequests = 300,
        _Stale = False,
        sendAllRequests = False,
        setupRateInitial = 100,
        teardownRateInitial = 100,
        gatewayArpRequestRate = 300,
        duplicateCheckingScope = 1
)

    #################################################
    # Network Specific Settings(overrides some of the session specific settings)
    #################################################
    # If the 'override' property is set to true the specific settings for this network will override the session specific settings
    my_ixNetEGTPPluginPortGroupData_SGW = Network2.getNetworkSpecificData("EGTPPlugin_SGW")

    my_ixNetEGTPPluginPortGroupData_SGW.activities.clear()

    

    my_ixNetEGTPPluginPortGroupData_SGW.associates.clear()

    

    my_ixNetEGTPPluginPortGroupData_SGW.config(
        sgiIPv4 = "22.22.22.22",
        itemType = "EGTPPluginPortGroupData_SGW",
        distributeUserPlaneIps = False,
        enableDynamicAllocation = True,
        enableDDN = False,
        responseCacheRotationInterval = 15,
        dDNTimeout = 20,
        enableResponseCache = True,
        fakeDualStack = False,
        sgiIPv6 = "::1616:1616",
        _Stale = False,
        pcpuLogLevel = "0",
        enableCreateBearerTFTHack = False,
        enableSGI = False,
        permitDuplicateIps = False,
        stackFunction = 1,
        publishStatistics = True,
        assignSameIpOnMultiport = True,
        enableGtpuSequenceNumber = False
)

    # If the 'override' property is set to true the specific settings for this network will override the session specific settings
    my_ixNetIxCatENodeBSimPortGroupData = Network1_1.getNetworkSpecificData("IxCatENodeBSimPlugin")

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
        autoDetectInstances = False,
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
    my_ixNetIPSecPortGroupData = Network1_1.getNetworkSpecificData("IPSecPlugin")

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

    #################################################
    # Create the test controller to run the test
    #################################################
    testController = IxLoad.new("ixTestController", outputDir = True
)

    

    testController.initPythonApi()

    testController.setResultDir("RESULTS/abo_1")

    Subscriber1_Network1_1.setCommunityCaptureParams(Test1, True)

    Network1_1.portList[0].setAnalyzerPartialCapture("False;8192")


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

    Subscriber1_Network1_1.removeAllPortsFromAnalyzer()

    Traffic4_Network2.removeAllPortsFromAnalyzer()

    IxLoad.delete(chassisChain)

    IxLoad.delete(Test1)

    IxLoad.delete(profileDirectory)

    IxLoad.delete(my_ixEventHandlerSettings)

    IxLoad.delete(my_ixViewOptions)

    IxLoad.delete(TrafficFlow1)

    IxLoad.delete(Originate)

    IxLoad.delete(Subscriber1_Network1_1)

    IxLoad.delete(Network1_1)

    IxLoad.delete(my_ixPortL1Settings)

    IxLoad.delete(Settings_6)

    IxLoad.delete(Filter_7)

    IxLoad.delete(GratARP_7)

    IxLoad.delete(TCP_6)

    IxLoad.delete(DNS_6)

    IxLoad.delete(SCTP_2)

    IxLoad.delete(Meshing_5)

    IxLoad.delete(Ethernet_6)

    IxLoad.delete(my_ixNetDataCenterSettings)

    IxLoad.delete(my_ixNetEthernetELMPlugin)

    IxLoad.delete(my_ixNetDualPhyPlugin)

    IxLoad.delete(MAC_VLAN_13)

    IxLoad.delete(UP_IP_10)

    IxLoad.delete(eNodeB_2)

    IxLoad.delete(MAC_VLAN_16)

    IxLoad.delete(IP_12)

    IxLoad.delete(User_Equipment_1)

    IxLoad.delete(my_ixNetIxCatENodeBSimNetworkActivity)

    IxLoad.delete(my_ixNetIxCatENodeBSimNetworkActivitySettings)

    IxLoad.delete(MAC_GNB)

    IxLoad.delete(IP_GNB)

    IxLoad.delete(MMEPool_R2)

    IxLoad.delete(eNB_R2)

    IxLoad.delete(my_ixNetIxCatENodeBSimResourceStatusReport)

    IxLoad.delete(my_ixNetIxCatENodeBSimLoadIndication)

    IxLoad.delete(my_ixNetIxCatENodeBSimMMEPoolEntry)

    IxLoad.delete(IP_R9)

    IxLoad.delete(MAC_R9)

    IxLoad.delete(VLAN_R12)

    IxLoad.delete(IP_R8)

    IxLoad.delete(MAC_R8)

    IxLoad.delete(VLAN_R11)

    IxLoad.delete(UE_R3)

    IxLoad.delete(my_ixNetIxCatENodeBSimCipheringAlgorithms)

    IxLoad.delete(my_ixNetIxCatENodeBSimUeFailureTesting)

    IxLoad.delete(my_ixNetIxCatENodeBSimUeNetworkCapabilityCIoT)

    IxLoad.delete(my_ixNetIxCatENodeBSimIntegrityAlgorithms)

    IxLoad.delete(IxCatENodeBSimUePCO_3)

    IxLoad.delete(my_ixNetIxCatENodeBSimApnEntry)

    IxLoad.delete(my_ixNetIxCatRNCIuPSQoSv1)

    IxLoad.delete(Activity_eNB_S1_MME_CP)

    IxLoad.delete(Timeline3)

    IxLoad.delete(my_ixNetIxCatENodeBSimCommandNegativeTestingNasEntry)

    IxLoad.delete(my_ixNetIxCatENodeBSimCommandNegativeTestingS1apEntry)

    IxLoad.delete(SubActivity_UE_R3)

    IxLoad.delete(Subscriber_Activity_HTTPClient1)

    IxLoad.delete(APN_1)

    IxLoad.delete(DedicatedBearer_2)

    IxLoad.delete(my_ixThinkCommand)

    IxLoad.delete(my_ixHttpHeaderString)

    IxLoad.delete(my_ixHttpHeaderString1)

    IxLoad.delete(my_ixHttpHeaderString2)

    IxLoad.delete(my_ixHttpHeaderString3)

    IxLoad.delete(DUT)

    IxLoad.delete(Terminate)

    IxLoad.delete(Traffic4_Network2)

    IxLoad.delete(Network2)

    IxLoad.delete(my_ixPortL2)

    IxLoad.delete(Settings_4)

    IxLoad.delete(Filter_5)

    IxLoad.delete(GratARP_5)

    IxLoad.delete(TCP_4)

    IxLoad.delete(DNS_4)

    IxLoad.delete(Meshing_3)

    IxLoad.delete(Ethernet_4)

    IxLoad.delete(my_ixNetDataCenterSettings1)

    IxLoad.delete(my_ixNetEthernetELMPlugin1)

    IxLoad.delete(my_ixNetDualPhyPlugin1)

    IxLoad.delete(MAC_VLAN_5)

    IxLoad.delete(DualStackIP_1)

    IxLoad.delete(SGW_S11_S1_U_1)

    IxLoad.delete(MAC_VLAN_11)

    IxLoad.delete(UP_IP_9)

    IxLoad.delete(MAC_VLAN_10)

    IxLoad.delete(CP_IP_8)

    IxLoad.delete(my_ixNetEGTPNetworkActivity_SGW)

    IxLoad.delete(my_ixNetEGTPNetworkActivitySettings_SGW)

    IxLoad.delete(SGW_R1)

    IxLoad.delete(IP_R11)

    IxLoad.delete(MAC_R10)

    IxLoad.delete(VLAN_R18)

    IxLoad.delete(IP_R12)

    IxLoad.delete(MAC_R11)

    IxLoad.delete(VLAN_R19)

    IxLoad.delete(IP_R10)

    IxLoad.delete(MAC_R12)

    IxLoad.delete(VLAN_R17)

    IxLoad.delete(PCRF_R1)

    IxLoad.delete(my_ixNetGTPNGQoSv1)

    IxLoad.delete(Activity_eGTP_Control_Plane)

    IxLoad.delete(_Match_Longest_)

    IxLoad.delete(Activity_FTPServer1)

    IxLoad.delete(_Match_Longest_1)

    IxLoad.delete(my_RealFileObject)

    IxLoad.delete(my_RealFileObject1)

    IxLoad.delete(my_RealFileObject2)

    IxLoad.delete(my_RealFileObject3)

    IxLoad.delete(my_RealFileObject4)

    IxLoad.delete(my_RealFileObject5)

    IxLoad.delete(my_RealFileObject6)

    IxLoad.delete(my_RealFileObject7)

    IxLoad.delete(my_RealFileObject8)

    IxLoad.delete(my_RealFileObject9)

    IxLoad.delete(my_RealFileObject10)

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

    IxLoad.delete(my_ixNetEGTPPluginSessionData_SGW)

    IxLoad.delete(my_ixNetEGTPQci2TosEntry_SGW)

    IxLoad.delete(my_ixNetEGTPQci3)

    IxLoad.delete(my_ixNetEGTPQci4)

    IxLoad.delete(my_ixNetEGTPQci5)

    IxLoad.delete(my_ixNetEGTPQci6)

    IxLoad.delete(my_ixNetEGTPQci7)

    IxLoad.delete(my_ixNetEGTPQci8)

    IxLoad.delete(my_ixNetEGTPQci9)

    IxLoad.delete(my_ixNetEGTPQci10)

    IxLoad.delete(my_ixNetEGTPPluginPortGroupData_SGW)

    IxLoad.delete(my_ixNetIxCatENodeBSimPortGroupData)

    IxLoad.delete(my_ixNetIPSecPortGroupData)

    IxLoad.delete(testController)



    #################################################
    # Disconnect / Release application lock
    #################################################
except Exception, e:
    print str(e)

IxLoad.delete(logEngine)
IxLoad.delete(logger)

IxLoad.disconnect()
